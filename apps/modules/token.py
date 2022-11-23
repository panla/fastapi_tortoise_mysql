import traceback
from typing import Tuple
from datetime import datetime, timedelta

import jwt
from fastapi import Request, Header, Depends
from tortoise.exceptions import OperationalError

from config import AuthenticConfig
from extensions import BadRequest, Unauthorized, NotFound, logger
from redis_ext import TokenRedis
from apps.models import User, AdminUser


class TokenResolver:
    EXTEND_MODEL_MAP = {'AdminUser': AdminUser}

    @classmethod
    def encode_auth_token(cls, user_id: int, extend_user_id: int, extend_model: str) -> Tuple[str, datetime, datetime]:
        """generate jwt token"""

        login_time = datetime.now()
        token_expired = login_time + timedelta(seconds=AuthenticConfig.ADMIN_TOKEN_EXP_DELTA)

        try:
            payload = {
                'exp': int(token_expired.timestamp()),
                'iat': int(login_time.timestamp()),
                'iss': 'ken',
                'data': {
                    'user_id': user_id,
                    'extend_user_id': extend_user_id,
                    'extend_model': extend_model,
                    'login_time': login_time.timestamp(),
                    'token_expired': token_expired.timestamp()
                }
            }
            token = jwt.encode(payload, AuthenticConfig.ADMIN_SECRETS, algorithm="HS256")
            return token, login_time, token_expired
        except Exception as e:
            raise BadRequest(message=str(e))

    @classmethod
    async def query_user(cls, user_id: int, extend_user_id: str, extend_model: str, **kwargs):
        """select query user, extend_user"""

        model_class = cls.EXTEND_MODEL_MAP.get(extend_model)
        if not model_class:
            raise BadRequest(message=f'Model {extend_model} error')

        user = await User.filter(id=user_id, is_delete=False).first()
        if not user:
            raise NotFound(f'User User.id = {user_id} is not exists or is deleted')

        extend_user = await model_class.filter(id=extend_user_id, user_id=user_id, is_delete=False).first()
        if not extend_user:
            raise NotFound(message=f'{extend_model} {extend_model}.id = {extend_user_id} is not exists or is deleted')

        return user, extend_user

    @classmethod
    async def _check_redis(cls, token: str, user: User, extend_model: str, extend_user_id: int):
        token_redis_op = TokenRedis()
        token_redis_op.name = f'{user.cellphone}:{extend_model}:{extend_user_id}'

        if not await token_redis_op.get() == token:
            raise Unauthorized(message='login expired, please login retry.')

    @classmethod
    async def decode_token(cls, request: Request, token: str):
        """check token"""

        try:
            secret = AuthenticConfig.ADMIN_SECRETS
            payload = jwt.decode(token, secret, algorithms='HS256', options={'verify_exp': True})
            if isinstance(payload, dict) and isinstance(payload.get('data'), dict):
                data: dict = payload.get('data')
                extend_model = data.get('extend_model')

                user, extend_user = await cls.query_user(**data)

                await cls._check_redis(token, user, extend_model, extend_user.id)

                # set/save user, extend_user on request.state
                request.state.user = user
                request.state.extend_user = extend_user
                return payload
        except jwt.PyJWTError:
            logger.error(traceback.format_exc())
            raise Unauthorized(message='login expired，please login retry！')
        except OperationalError:
            logger.error(traceback.format_exc())
            raise Unauthorized(message='database connect exception，please request retry')


async def get_current_admin_user(request: Request, x_token: str = Header(..., description='token')):
    """decode user, admin_user from request header"""

    await TokenResolver.decode_token(request, x_token)
    return request.state.extend_user


current_admin_user = Depends(get_current_admin_user)
