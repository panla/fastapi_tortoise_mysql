import sys

from tortoise import Tortoise

from tests import BASE_DIR
from .pre_data import users, admin_users, books, cars, orders, phones, questions

sys.path.append(BASE_DIR)

from config import ORM_TEST_MIGRATE_CONF

from apps.models import User, AdminUser, Book, Car, Order, Phone, Question


def build_instances(Model, dic_list: list):
    for per_dic in dic_list:
        yield Model(**per_dic)


async def create_data():
    batch_size = 5

    await User.bulk_create(objects=build_instances(User, users), batch_size=batch_size)
    await AdminUser.bulk_create(objects=build_instances(AdminUser, admin_users), batch_size=batch_size)
    await Book.bulk_create(objects=build_instances(Book, books), batch_size=batch_size)
    await Car.bulk_create(objects=build_instances(Car, cars), batch_size=batch_size)
    await Order.bulk_create(objects=build_instances(Order, orders), batch_size=batch_size)
    await Phone.bulk_create(objects=build_instances(Phone, phones), batch_size=batch_size)
    await Question.bulk_create(objects=build_instances(Question, questions), batch_size=batch_size)
    print('完成预创建数据')


async def generate_db():
    await Tortoise.init(
        config=ORM_TEST_MIGRATE_CONF,
        _create_db=True
    )
    await Tortoise.generate_schemas()

    await create_data()
    print('完成创建数据库与表')


async def delete_database():
    await Tortoise.init(
        config=ORM_TEST_MIGRATE_CONF,
    )
    await Tortoise._drop_databases()
    print('完成删除数据库')
