__all__ = [
    'create_database', 'delete_database'
]

from pathlib import Path

from tortoise import Tortoise

from tests import ORM_TEST_MIGRATE_CONF, BASE_DIR
from tests import User, AdminUser, Book, Car, Order, Phone, Question
from tests.utils import JsonFileOperator


def _build_instances(model_class, file: str):
    file = Path(BASE_DIR).joinpath(f'tests/fixture_data/{file}')
    for per_dic in JsonFileOperator(file).read():
        yield model_class(**per_dic)


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
