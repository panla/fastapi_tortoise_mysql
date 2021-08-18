from tortoise import Tortoise

from tests import ORM_TEST_MIGRATE_CONF
from tests import User, AdminUser, Book, Car, Order, Phone, Question
from tests.pre_data import users, admin_users, books, cars, orders, phones, questions


def build_instances(Model, dic_list: list):
    for per_dic in dic_list:
        yield Model(**per_dic)


async def write_data():
    batch_size = 5

    await User.bulk_create(objects=build_instances(User, users), batch_size=batch_size)
    await AdminUser.bulk_create(objects=build_instances(AdminUser, admin_users), batch_size=batch_size)
    await Book.bulk_create(objects=build_instances(Book, books), batch_size=batch_size)
    await Car.bulk_create(objects=build_instances(Car, cars), batch_size=batch_size)
    await Order.bulk_create(objects=build_instances(Order, orders), batch_size=batch_size)
    await Phone.bulk_create(objects=build_instances(Phone, phones), batch_size=batch_size)
    await Question.bulk_create(objects=build_instances(Question, questions), batch_size=batch_size)
    print('write pre data over')


async def create_database():
    # create database
    await Tortoise.init(
        config=ORM_TEST_MIGRATE_CONF,
        _create_db=True
    )
    print('create database over')

    # create tables
    await Tortoise.generate_schemas()
    print('create tables over')

    await write_data()


async def delete_database():
    # link to database
    await Tortoise.init(
        config=ORM_TEST_MIGRATE_CONF,
    )

    # drop database
    await Tortoise._drop_databases()
    print('drop database over')
