__all__ = [
    'generate_token'
]

import os

from tortoise import Tortoise

from tests import AuthenticConfig, ORM_TEST_MIGRATE_CONF
from tests import NotFound, BadRequest, TokenResolver
from tests import User, AdminUser
from tests import TokenRedis

EXTEND_MODEL_MAP = {'AdminUser': AdminUser, 'User': User}


async def authentic_test(cellphone: str, extend_model: str = 'AdminUser'):
    model_class = EXTEND_MODEL_MAP.get(extend_model)
    if not model_class:
        raise BadRequest(message=f'Model {extend_model} error')

    user = await User.get_or_none(cellphone=cellphone, is_delete=False)
    if not user:
        raise NotFound(f'User User.cellphone = {cellphone} is not exists or is deleted')

    extend_user = await model_class.filter(user_id=user.id, is_delete=False).first()
    if not extend_user:
        raise NotFound(message=f'{extend_model} User.cellphone = {cellphone} is not exists or is deleted')

    token, login_time, token_expired = TokenResolver.encode_auth_token(user.id, extend_user.id, 'AdminUser')
    extend_user.login_time = login_time
    extend_user.token_expired = token_expired
    await extend_user.save()

    token_redis_op = TokenRedis()
    token_redis_op.name = f'{user.cellphone}:{extend_model}:{extend_user.id}'
    await token_redis_op.set(token, ex=AuthenticConfig.ADMIN_TOKEN_EXP_DELTA)

    return token


async def generate_token():
    """create a super_admin_user token and save it into os.environ"""

    # link to database
    await Tortoise.init(config=ORM_TEST_MIGRATE_CONF)

    os.environ['AdminUserTestToken'] = await authentic_test('10000000001')


def remove_token():
    """remove os env test token

    TODO remove from redis
    """

    del os.environ['AdminUserTestToken']
    print('remove env AdminUserTestToken')
