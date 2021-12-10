import os
import traceback
from datetime import datetime, timedelta

import jwt
from fastapi import Request, Header, Depends
from tortoise.exceptions import OperationalError

from config import Config
from extensions import BadRequest, Unauthorized, NotFound, logger
from redis_ext import TokenRedis
from apps.models import User, AdminUser


class TokenResolver:

    EXTEND_MODEL_MAP = {'AdminUser': AdminUser}

    @classmethod
    def encode_auth_token(cls, user_id: int, extend_user_id: int, extend_model: str):
        """generate jwt token"""

        login_time = datetime.now()
        token_expired = login_time + timedelta(seconds=Config.authentic.ADMIN_TOKEN_EXP_DELTA)

        try:
            payload = {
                'exp': token_expired,
                'iat': login_time,
                'iss': 'ken',
                'data': {
                    'user_id': user_id,
                    'extend_user_id': extend_user_id,
                    'extend_model': extend_model,
                    'login_time': login_time.timestamp(),
                    'token_expired': token_expired.timestamp()
                    }
            }
            token = jwt.encode(payload, Config.authentic.ADMIN_SECRETS, algorithm="HS256")
            return token, login_time, token_expired
        except Exception as e:
            raise BadRequest(message=str(e))

    @classmethod
    async def query_user(cls, user_id: int, extend_user_id: str, extend_model: str, **kwargs):
        """select query user, extend_user"""

        Model = cls.EXTEND_MODEL_MAP.get(extend_model)
        if not Model:
            raise BadRequest(message=f'Model {extend_model} error')

        user = await User.filter(id=user_id, is_delete=False).first()
        if not user:
            raise NotFound(f'User User.id = {user_id} is not exists or is deleted')

        extend_user = await Model.filter(id=extend_user_id, user_id=user_id, is_delete=False).first()
        if not extend_user:
            raise NotFound(message=f'{extend_model} {extend_model}.id = {extend_user_id} is not exists or is deleted')

        return user, extend_user

    @staticmethod
    def check_timeout(extend_user, now: float, data: dict):
        """check the token is expired or not"""

        a = not (extend_user.login_time and extend_user.token_expired)
        b = (now - data.get('token_expired')) > 1
        # now > the expired_time in JWT (had expired)
        c = extend_user.login_time.timestamp() - data.get('login_time') > 1
        # the login time in db > the login time in JWT (there is a new login, this token is expired)
        d = data.get('token_expired') - extend_user.token_expired.timestamp() > 1
        # the expired time in db < the expired time in JWT (had expired)
        _lis = [a, b, c, d]
        if any(_lis):
            logger.error([a, b, c, d])
            raise Unauthorized(message='login expired, please login retry.')

    @classmethod
    async def _check_redis(cls, token: str, user: User, extend_model: str, extend_user_id: int):
        code_env = os.environ.get('CODE_ENV', 'prd')
        if code_env == 'test':
            token_redis_op = TokenRedis(user.cellphone, extend_model, extend_user_id)
        else:
            token_redis_op = TokenRedis(user.id, extend_model, extend_user_id)
        if not await token_redis_op.get() == token:
            raise Unauthorized(message='login expired, please login retry.')

    @classmethod
    async def decode_token(cls, request: Request, token: str):
        """check token"""

        try:
            secret = Config.authentic.ADMIN_SECRETS
            payload = jwt.decode(token, secret, algorithms='HS256', options={'verify_exp': True})
            if isinstance(payload, dict) and isinstance(payload.get('data'), dict):
                data: dict = payload.get('data')
                extend_model = data.get('extend_model')

                user, extend_user = await cls.query_user(**data)

                await cls._check_redis(token, user, extend_model, extend_user.id)

                request.state.user = user
                request.state.extend_user = extend_user
                return payload
        except jwt.PyJWTError:
            raise Unauthorized(message='login expired，please login retry！')
        except OperationalError:
            logger.error(traceback.format_exc())
            raise Unauthorized(message='database connect exception，please request retry')


async def get_current_admin_user(request: Request, x_token: str = Header(..., description='token')):
    """decode user, admin_user from request header"""

    await TokenResolver.decode_token(request, x_token)
    return request.state.extend_user


current_admin_user = Depends(get_current_admin_user)
