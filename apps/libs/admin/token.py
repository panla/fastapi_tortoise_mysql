import time
from datetime import datetime, timedelta

import jwt
from fastapi import Request, Header

import config
from apps.utils import redis_pool
from apps.utils.response import resp_201, resp_400, resp_401, resp_404
from apps.models import User, AdminUser


async def authentic(request: Request, cellphone: str, code: str):
    redis = await redis_pool()
    if code == await redis.get(cellphone):
        user = await User.get_or_none(cellphone=cellphone)
        if not user or user.is_delete:
            return resp_404('该用户不存在或被删除')
        admin_user = await AdminUser.get_or_none(user_id=user.id)
        if not admin_user or admin_user.is_delete:
            return resp_404('该管理员不存在或被删除')
        token, login_time, token_expired = encode_auth_token(user.id)
        admin_user.login_time = login_time
        admin_user.token_expired = token_expired
        await admin_user.save()
        data = {'token': token, 'user_id': user.id, 'admin_user_id': admin_user.id}
        return data
    return resp_400('验证码错误')


def encode_auth_token(account_id):
    """生成认证Token"""

    login_time = datetime.now()
    token_expired = login_time + timedelta(seconds=config.TOKEN_EXP_DELTA_ADMIN)

    try:
        payload = {
            'exp': token_expired,
            'iat': login_time,
            'iss': 'ken',
            'data': {'id': account_id, 'login_time': login_time.timestamp(), 'token_expired': token_expired.timestamp()}
        }
        token = jwt.encode(payload, config.ADMIN_SECRETS, algorithm="HS256")
        return token, login_time, token_expired
    except Exception as e:
        return resp_400(str(e))


async def decode_auth_token(request: Request, token: str):
    """校验token"""

    try:
        payload = jwt.decode(token, config.ADMIN_SECRETS, algorithms='HS256', options={'verify_exp': True})
        if isinstance(payload, dict) and isinstance(payload.get('data'), dict):

            data: dict = payload.get('data')
            user = await User.get_or_none(id=data.get('id'))
            admin_user = await AdminUser.get_or_none(user_id=data.get('id'))
            now = time.time()

            if not admin_user or admin_user.is_delete:
                return resp_401('该管理员不存在')
            if not (admin_user.login_time and admin_user.token_expired):
                return resp_401('请重新登录')
            if data.get('token_expired') < now:
                return resp_401('请重新登录')
            if data.get('login_time') < admin_user.login_time.timestamp():
                return resp_401('请重新登录')
            if data.get('token_expired') > admin_user.token_expired.timestamp():
                return resp_401('请重新登录')

            request.state.admin_user = admin_user
            request.state.user = user
            return payload
    except Exception as exc:
        return resp_401('请重新登录')


async def get_current_admin_user(request: Request, x_token: str = Header(..., description='token')):
    await decode_auth_token(request, x_token)
    return request.state.admin_user
