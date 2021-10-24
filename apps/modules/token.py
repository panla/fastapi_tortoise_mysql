import time
from datetime import datetime, timedelta
import traceback

import jwt
from fastapi import Request, Header
from tortoise.exceptions import OperationalError

from config import Config
from extensions import BadRequest, Unauthorized, NotFound, logger
from redis_ext import SMSCodeRedis
from apps.models import User, AdminUser


class TokenResolver:

    EXTEND_MODEL_MAP = {'AdminUser': AdminUser, 'User': User}

    @classmethod
    async def authentic(cls, cellphone: str, code: str, extend_model: str):
        """the entrance to get auth token"""

        redis_client = SMSCodeRedis(cellphone)
        if code == await redis_client.get():
            user = await User.filter(cellphone=cellphone, is_delete=False).first()
            if not user:
                raise NotFound(f'User User.cellphone = {cellphone} is not exists or is deleted')

            Model = cls.EXTEND_MODEL_MAP.get(extend_model)
            if not Model:
                raise BadRequest(message=f'Model {extend_model} error')

            extend_user = await Model.filter(user_id=user.id, is_delete=False).first()

            if not extend_user:
                raise NotFound(message=f'{extend_model} User.cellphone = {cellphone} is not exists or is deleted')

            token, login_time, token_expired = cls.encode_auth_token(user.id, extend_user.id, 'AdminUser')
            extend_user.login_time = login_time
            extend_user.token_expired = token_expired
            await extend_user.save()

            return {'token': token, 'user_id': user.id, 'extend_user_id': extend_user.id, 'extend_model': 'AdminUser'}
        raise BadRequest(message='SMS Code error')

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

        user = await User.filter(id=user_id, is_delete=False).first()
        if not user:
            raise NotFound(f'User User.id = {user_id} is not exists or is deleted')

        Model = cls.EXTEND_MODEL_MAP.get(extend_model)
        if not Model:
            raise BadRequest(message=f'Model {extend_model} error')

        extend_user = await Model.filter(id=extend_user_id, user_id=user_id, is_delete=False).first()

        if not extend_user:
            raise NotFound(message=f'{extend_model} {extend_model}.id = {extend_user_id} is not exists or is deleted')

        return user, extend_user 

    @staticmethod
    def check_timeout(extend_user, now: float, data: dict):
        """check the token is expired or not"""

        a = not (extend_user.login_time and extend_user.token_expired)
        b = data.get('token_expired') < now
        c = data.get('login_time') < extend_user.login_time.timestamp()
        d = data.get('token_expired') > extend_user.token_expired.timestamp()
        if any([a, b, c, d]):
            logger.error([a, b, c, d])
            raise Unauthorized(message='login expired，please login retry。')

    @classmethod
    async def decode_token(cls, request: Request, token: str):
        """check token"""

        now = time.time()
        try:
            secret = Config.authentic.ADMIN_SECRETS
            payload = jwt.decode(token, secret, algorithms='HS256', options={'verify_exp': True})
            if isinstance(payload, dict) and isinstance(payload.get('data'), dict):
                data: dict = payload.get('data')

                user, extend_user = await cls.query_user(**data)

                cls.check_timeout(extend_user, now, data)

                request.state.extend_user = extend_user
                request.state.user = user
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
