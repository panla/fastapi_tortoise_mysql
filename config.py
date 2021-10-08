__all__ = [
    'Config', 'ORM_LINK_CONF', 'ORM_MIGRATE_CONF', 'ORM_TEST_MIGRATE_CONF'
]

import os

from starlette.config import Config as StarletConfig

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

config = StarletConfig('.env')

CODE_ENV = config('CODE_ENV', default='prd')


class BaseConfig(object):
    ###############################################################################################
    ## log
    LOG_LEVEL = config('LOG_LEVEL', default='DEBUG')
    LOG_PATH = config('LOG_PATH')

    ###############################################################################################
    ## service on down
    # openapi swagger
    INCLUDE_IN_SCHEMA = config('INCLUDE_IN_SCHEMA', cast=bool, default=True)

    # socket.io on
    SOCKET_IO_ON = config('SOCKET_IO_ON', cast=bool, default=False)

    ###############################################################################################
    ## authentic token
    ADMIN_SECRETS = config('ADMIN_SECRETS')
    TOKEN_EXP_DELTA_ADMIN = config('TOKEN_EXP_DELTA_ADMIN', cast=int, default=86400)

    ###############################################################################################
    ## socket.io
    SOCKET_IO_NAMESPACE = config('SOCKET_IO_NAMESPACE', cast=str, default='/')
    SOCKET_IO_PATH = config('SOCKET_IO_PATH', cast=str, default='socket.io')
    SOCKET_IO_MOUNT = config('SOCKET_IO_MOUNT', cast=str, default='/')

    ###############################################################################################
    ## mysql database

    DB_POOL_RECYCLE = config('DB_POOL_RECYCLE', cast=int, default=1800)

    DB_USER = 'root'
    DB_PASSWD = 'DB_PASSWD'
    DB_HOST = '127.0.0.1'
    DB_PORT = 3306
    DB_DATABASE = 'DB_DATABASE'
    DB_MAX_SIZE = 5

    ###############################################################################################
    ## orm
    def _base_orm_conf(self, apps: dict) -> dict:
        return {
            'connections': {
                'default': {
                    'engine': 'tortoise.backends.mysql',
                    'credentials': {
                        'host': self.DB_HOST,
                        'port': self.DB_PORT,
                        'user': self.DB_USER,
                        'password': self.DB_PASSWD,
                        'database': self.DB_DATABASE,
                        'minsize': 1,
                        'maxsize': self.DB_MAX_SIZE,
                        'charset': 'utf8mb4',
                        'pool_recycle': self.DB_POOL_RECYCLE
                    }
                }
            },
            'apps': apps,
            'use_tz': False,
            'timezone': 'Asia/Shanghai'
        }

    @property
    def orm_link_conf(self) -> dict:
        orm_apps_settings = {
            'models': {
                'models': [
                    'aerich.models',
                    'apps.models.models'
                ],
                'default_connection': 'default',
            },
        }
        return self._base_orm_conf(orm_apps_settings)

    @property
    def orm_migrate_conf(self) -> dict:
        orm_apps_settings = {
            'models': {
                'models': [
                    'aerich.models',
                    'apps.models.models'
                ],
                'default_connection': 'default',
            },
        }
        return self._base_orm_conf(orm_apps_settings)

    @property
    def orm_test_migrate_conf(self) -> dict:
        orm_apps_settings = {
            'models': {
                'models': [
                    'aerich.models',
                    'apps.models.models'
                ],
                'default_connection': 'default',
            },
        }
        return self._base_orm_conf(orm_apps_settings)


class PrdConfig(BaseConfig):
    ###############################################################################################
    ## redis
    REDIS_HOST = config('REDIS_HOST', default='127.0.0.1')
    REDIS_PORT = config('REDIS_PORT', cast=int, default=6379)
    REDIS_PASSWD = config('REDIS_PASSWD', default='')

    ###############################################################################################
    ## mysql database
    DB_USER = config('DB_USER', default='root')
    DB_PASSWD = config('DB_PASSWD')
    DB_HOST = config('DB_HOST', default='127.0.0.1')
    DB_PORT = config('DB_PORT', cast=int, default=3306)
    DB_DATABASE = config('DB_DATABASE')
    DB_MAX_SIZE = config('DB_MAX_SIZE', cast=int, default=5)


class TestConfig(BaseConfig):
    ###############################################################################################
    ## redis
    REDIS_HOST = config('TEST_REDIS_HOST', default='127.0.0.1')
    REDIS_PORT = config('TEST_REDIS_PORT', cast=int, default=6379)
    REDIS_PASSWD = config('TEST_REDIS_PASSWD', default='')

    ###############################################################################################
    ## mysql database
    DB_USER = config('TEST_DB_USER', default='root')
    DB_PASSWD = config('TEST_DB_PASSWD')
    DB_HOST = config('TEST_DB_HOST', default='127.0.0.1')
    DB_PORT = config('TEST_DB_PORT', cast=int, default=3306)
    DB_DATABASE = config('TEST_DB_DATABASE')
    DB_MAX_SIZE = config('TEST_DB_MAX_SIZE', cast=int, default=2)


if CODE_ENV == 'prd':
    Config = PrdConfig
else:
    Config = TestConfig

ORM_LINK_CONF = Config().orm_link_conf
ORM_MIGRATE_CONF = Config().orm_migrate_conf
ORM_TEST_MIGRATE_CONF = Config().orm_test_migrate_conf
