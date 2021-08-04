__all__ = [
    'authentic', 'get_current_admin_user'
]

import time
from datetime import datetime, timedelta
import traceback

import jwt
from fastapi import Request, Header
from tortoise.exceptions import OperationalError

from config import Config
from apps.extensions import BadRequest, Unauthorized, NotFound
from apps.redis_ext import SMSCodeRedis
from apps.utils import logger
from apps.models import User, AdminUser


async def authentic(cellphone: str, code: str):
    """the entrance to get auth token"""

    redis_client = SMSCodeRedis(cellphone)
    if code == await redis_client.get():
        user = await User.get_or_none(cellphone=cellphone)
        if not user or user.is_delete:
            raise NotFound(f'User User.cellphone = {cellphone} is not exists or is deleted')

        admin_user = await user.admin_user

        if not admin_user or admin_user.is_delete:
            raise NotFound(message=f'AdminUser User.cellphone = {cellphone} is not exists or is deleted')

        token, login_time, token_expired = encode_auth_token(user.id)
        admin_user.login_time = login_time
        admin_user.token_expired = token_expired
        await admin_user.save()

        return {'token': token, 'user_id': user.id, 'admin_user_id': admin_user.id}
    raise BadRequest(message='SMS Code error')


def encode_auth_token(account_id):
    """generate jwt token"""

    login_time = datetime.now()
    token_expired = login_time + timedelta(seconds=Config.TOKEN_EXP_DELTA_ADMIN)

    try:
        payload = {
            'exp': token_expired,
            'iat': login_time,
            'iss': 'ken',
            'data': {'id': account_id, 'login_time': login_time.timestamp(), 'token_expired': token_expired.timestamp()}
        }
        token = jwt.encode(payload, Config.ADMIN_SECRETS, algorithm="HS256")
        return token, login_time, token_expired
    except Exception as e:
        raise BadRequest(message=str(e))


async def query_admin_user(user_id: int):
    """select query user, admin_user

    当数据库 wait_timeout 时 pymysql 可能会抛错, 需要做重复查询
    """

    admin_user = await AdminUser.filter(user_id=user_id).first()
    if not admin_user or admin_user.is_delete:
        raise NotFound(message=f'AdminUser User.id = {user_id} is not exists or is deleted')
    user = await admin_user.user
    if not user or user.is_delete:
        raise NotFound(message=f'User User.id = {user_id} is not exists or is deleted')

    return admin_user, user


def check_timeout(admin_user: AdminUser, now: float, data: dict):
    """check the token is expired or not"""

    a = not (admin_user.login_time and admin_user.token_expired)
    b = data.get('token_expired') < now
    c = data.get('login_time') < admin_user.login_time.timestamp()
    d = data.get('token_expired') > admin_user.token_expired.timestamp()
    if any([a, b, c, d]):
        logger.error([a, b, c, d])
        raise Unauthorized(message='登录过期请重新登录')


async def decode_admin_token(request: Request, token: str):
    """check token"""

    now = time.time()
    try:
        payload = jwt.decode(token, Config.ADMIN_SECRETS, algorithms='HS256', options={'verify_exp': True})
        if isinstance(payload, dict) and isinstance(payload.get('data'), dict):
            data: dict = payload.get('data')

            admin_user, user = await query_admin_user(data.get('id'))

            check_timeout(admin_user, now, data)

            request.state.admin_user = admin_user
            request.state.user = user
            return payload
    except jwt.PyJWTError:
        raise Unauthorized(message='pyjwt check token error, please login retry')
    except OperationalError:
        logger.error(traceback.format_exc())
        raise Unauthorized(message='database connect exception，please request retry')


async def get_current_admin_user(request: Request, x_token: str = Header(..., description='token')):
    """decode user, admin_user from request header"""

    await decode_admin_token(request, x_token)
    return request.state.admin_user
