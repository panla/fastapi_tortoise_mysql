import sys

from tortoise import Tortoise

from tests import BASE_DIR
sys.path.append(BASE_DIR)

from config import MIGRATE_TORTOISE_ORM

from apps.models import User, Car, AdminUser


async def create_data():
    await Car(brand='宝马', price='30000000').save()
    user = User(name='athena', cellphone='12345678911')
    await user.save()
    await AdminUser(user_id=user.id).save()


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
