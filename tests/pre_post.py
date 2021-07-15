import sys

from tortoise import Tortoise

from tests import BASE_DIR
from .pre_data import users, admin_users, books, cars, orders, phones, questions

sys.path.append(BASE_DIR)

from config import MIGRATE_TORTOISE_ORM

from apps.models import User, AdminUser, Book, Car, Order, Phone, Question


def build_instances(Model, dic_list: list):
    _lis = list()
    for per_dic in dic_list:
        _lis.append(Model(**per_dic))
    return _lis


async def create_data():
    await User.bulk_create(objects=build_instances(User, users), batch_size=5)
    print('创建完 users')
    await AdminUser.bulk_create(objects=build_instances(AdminUser, admin_users), batch_size=5)
    print('创建完 admin_users')
    await Book.bulk_create(objects=build_instances(Book, books), batch_size=5)
    print('创建完 books')
    await Car.bulk_create(objects=build_instances(Car, cars), batch_size=5)
    print('创建完 cars')
    await Order.bulk_create(objects=build_instances(Order, orders), batch_size=5)
    print('创建完 orders')
    await Phone.bulk_create(objects=build_instances(Phone, phones), batch_size=5)
    print('创建完 phones')
    await Question.bulk_create(objects=build_instances(Question, questions), batch_size=5)
    print('创建完 questions')


async def generate_db():
    await Tortoise.init(
        config=MIGRATE_TORTOISE_ORM,
        _create_db=True
    )
    await Tortoise.generate_schemas()

    await create_data()


async def delete_database():
    await Tortoise.init(
        config=MIGRATE_TORTOISE_ORM,
    )
    await Tortoise._drop_databases()
