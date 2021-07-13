__all__ = [
    'Config', 'TORTOISE_ORM'
]

from starlette.config import Config as StarletConfig

config = StarletConfig('.env')

CODE_ENV = config('CODE_ENV', default='prd')


class BaseConfig(object):
    LOG_LEVEL = config('LOG_LEVEL', default='DEBUG')
    LOG_PATH = config('LOG_PATH')
    INCLUDE_IN_SCHEMA = config('include_in_schema', cast=bool, default=True)

    ADMIN_SECRETS = config('ADMIN_SECRETS')
    TOKEN_EXP_DELTA_ADMIN = config('TOKEN_EXP_DELTA_ADMIN', cast=int, default=86400)


class PrdConfig(BaseConfig):
    REDIS_HOST = config('REDIS_HOST', default='127.0.0.1')
    REDIS_PORT = config('REDIS_PORT', cast=int, default=6379)
    REDIS_PASSWD = config('REDIS_PASSWD', default='')

    DB_USER = config('DB_USER', default='root')
    DB_PASSWD = config('DB_PASSWD')
    DB_HOST = config('DB_HOST', default='127.0.0.1')
    DB_PORT = config('DB_PORT', cast=int, default=3306)
    DB_DATABASE = config('DB_DATABASE')
    DB_MAX_SIZE = config('DB_MAX_SIZE', cast=int, default=5)


class TestConfig(BaseConfig):
    REDIS_HOST = config('REDIS_HOST', default='127.0.0.1')
    REDIS_PORT = config('REDIS_PORT', cast=int, default=6379)
    REDIS_PASSWD = config('REDIS_PASSWD', default='')

    DB_USER = config('DB_USER', default='root')
    DB_PASSWD = config('DB_PASSWD')
    DB_HOST = config('DB_HOST', default='127.0.0.1')
    DB_PORT = config('DB_PORT', cast=int, default=3306)
    DB_DATABASE = config('DB_DATABASE')
    DB_MAX_SIZE = config('DB_MAX_SIZE', cast=int, default=2)


def get_tortoise_orm_conf(instance):
    return {
        'connections': {
            'default': {
                'engine': 'tortoise.backends.mysql',
                'credentials': {
                    'database': instance.DB_DATABASE,
                    'host': instance.DB_HOST,
                    'password': instance.DB_PASSWD,
                    'port': instance.DB_PORT,
                    'user': instance.DB_USER,
                    'minsize': 1,
                    'maxsize': instance.DB_MAX_SIZE,
                    'charset': 'utf8mb4'
                }
            }
        },
        'apps': {
            'models': {
                'models': [
                    'aerich.models',
                    'apps.models.__init__'
                ],
                'default_connection': 'default',
            },
        },
        'use_tz': False,
        'timezone': 'Asia/Shanghai'
    }


if CODE_ENV == 'prd':
    Config = PrdConfig
else:
    Config = TestConfig

TORTOISE_ORM = get_tortoise_orm_conf(Config)
