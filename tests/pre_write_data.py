__all__ = [
    'create_database', 'delete_database', 'generate_token'
]

import os

from tortoise import Tortoise

from tests import ORM_TEST_MIGRATE_CONF, BASE_DIR
from tests import NotFound, encode_auth_token
from tests import User, AdminUser, Book, Car, Order, Phone, Question
from tests.utils import read_json_file


async def authentic_test(cellphone: str):
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
    return token


def _build_instances(Model, file: str):
    file = os.path.join(BASE_DIR, f'tests/fixture_data/{file}')
    for per_dic in read_json_file(file):
        yield Model(**per_dic)


async def _write_data():
    batch_size = 5

    await User.bulk_create(objects=_build_instances(User, 'users.json'), batch_size=batch_size)
    await AdminUser.bulk_create(objects=_build_instances(AdminUser, 'admin_users.json'), batch_size=batch_size)
    await Book.bulk_create(objects=_build_instances(Book, 'books.json'), batch_size=batch_size)
    await Car.bulk_create(objects=_build_instances(Car, 'cars.json'), batch_size=batch_size)
    await Order.bulk_create(objects=_build_instances(Order, 'orders.json'), batch_size=batch_size)
    await Phone.bulk_create(objects=_build_instances(Phone, 'phones.json'), batch_size=batch_size)
    await Question.bulk_create(objects=_build_instances(Question, 'questions.json'), batch_size=batch_size)
    print('write pre data over')


async def create_database():
    """create database and create tables"""

    # create database
    await Tortoise.init(config=ORM_TEST_MIGRATE_CONF, _create_db=True)
    print('create database over')

    # create tables
    await Tortoise.generate_schemas()
    print('create tables over')

    await _write_data()


async def delete_database():
    """drop database"""

    # link to database
    await Tortoise.init(config=ORM_TEST_MIGRATE_CONF)

    # drop database
    await Tortoise._drop_databases()
    print('drop database over')


async def generate_token():
    """create a super_admin_user token and save it into os.environ"""

    # link to database
    await Tortoise.init(config=ORM_TEST_MIGRATE_CONF)

    os.environ['AdminUserTestToken'] = await authentic_test('10000000001')
