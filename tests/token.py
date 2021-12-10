__all__ = [
    'generate_token'
]

import os

from tortoise import Tortoise

from tests import Config, ORM_TEST_MIGRATE_CONF
from tests import NotFound, BadRequest, TokenResolver
from tests import User, AdminUser
from tests import TokenRedis


EXTEND_MODEL_MAP = {'AdminUser': AdminUser, 'User': User}


async def authentic_test(cellphone: str, extend_model: str = 'AdminUser'):
    user = await User.get_or_none(cellphone=cellphone)
    if not user or user.is_delete:
        raise NotFound(f'User User.cellphone = {cellphone} is not exists or is deleted')

    Model = EXTEND_MODEL_MAP.get(extend_model)
    if not Model:
        raise BadRequest(message=f'Model {extend_model} error')

    extend_user = await Model.filter(user_id=user.id, is_delete=False).first()

    if not extend_user:
        raise NotFound(message=f'{extend_model} User.cellphone = {cellphone} is not exists or is deleted')

    token, login_time, token_expired = TokenResolver.encode_auth_token(user.id, extend_user.id, 'AdminUser')
    extend_user.login_time = login_time
    extend_user.token_expired = token_expired
    await extend_user.save()

    token_redis_op = TokenRedis(user.cellphone, extend_model, extend_user.id)
    await token_redis_op.set(token, ex=Config.authentic.ADMIN_TOKEN_EXP_DELTA)

    return token


async def generate_token():
    """create a super_admin_user token and save it into os.environ"""

    # link to database
    await Tortoise.init(config=ORM_TEST_MIGRATE_CONF)

    os.environ['AdminUserTestToken'] = await authentic_test('10000000001')
