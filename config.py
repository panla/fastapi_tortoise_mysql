from starlette.config import Config

config = Config('.env')

CODE_ENV = config('CODE_ENV', default='prd')

REDIS_HOST = config('REDIS_HOST', default='127.0.0.1')
REDIS_PORT = config('REDIS_PORT', cast=int, default=6379)
REDIS_PASSWD = config('REDIS_PASSWD', default='')

TEST_REDIS_HOST = config('TEST_REDIS_HOST', default='127.0.0.1')
TEST_REDIS_PORT = config('TEST_REDIS_PORT', cast=int, default=6379)
TEST_REDIS_PASSWD = config('TEST_REDIS_PASSWD', default='')

DB_USER = config('DB_USER', default='root')
DB_PASSWD = config('DB_PASSWD')
DB_HOST = config('DB_HOST', default='127.0.0.1')
DB_PORT = config('DB_PORT', cast=int, default=3306)
DB_DATABASE = config('DB_DATABASE')
DB_MAX_SIZE = config('DB_MAX_SIZE', cast=int, default=5)

TEST_DB_USER = config('DB_USER', default='root')
TEST_DB_PASSWD = config('DB_PASSWD')
TEST_DB_HOST = config('DB_HOST', default='127.0.0.1')
TEST_DB_PORT = config('DB_PORT', cast=int, default=3306)
TEST_DB_DATABASE = config('DB_DATABASE')
TEST_DB_MAX_SIZE = config('DB_MAX_SIZE', cast=int, default=2)

LOG_LEVEL = config('LOG_LEVEL', default='DEBUG')
LOG_PATH = config('LOG_PATH')
INCLUDE_IN_SCHEMA = config('include_in_schema', cast=bool, default=True)

if CODE_ENV == 'test':
    REDIS_HOST = TEST_REDIS_HOST
    REDIS_PORT = TEST_REDIS_PORT
    REDIS_PASSWD = TEST_REDIS_PASSWD

    DB_USER = TEST_DB_USER
    DB_PASSWD = TEST_DB_PASSWD
    DB_HOST = TEST_DB_HOST
    DB_PORT = TEST_DB_PORT
    DB_DATABASE = TEST_DB_DATABASE
    DB_MAX_SIZE = TEST_DB_MAX_SIZE

TORTOISE_ORM = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'database': DB_DATABASE,
                'host': DB_HOST,
                'password': DB_PASSWD,
                'port': DB_PORT,
                'user': DB_USER,
                'minisize': 1,
                'maxsize': DB_MAX_SIZE,
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

ADMIN_SECRETS = config('ADMIN_SECRETS')
TOKEN_EXP_DELTA_ADMIN = config('TOKEN_EXP_DELTA_ADMIN', cast=int, default=86400)
include_in_schema = INCLUDE_IN_SCHEMA
