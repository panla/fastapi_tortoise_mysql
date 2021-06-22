from starlette.config import Config

config = Config('.env')

CODE_ENV = config('CODE_ENV', default='prd')

REDIS_HOST = config('REDIS_HOST', default='127.0.0.1')
REDIS_PORT = config('REDIS_PORT', cast=int, default=6379)
REDIS_PASSWD = config('REDIS_PASSWD', default='')

TEST_REDIS_HOST = config('TEST_REDIS_HOST', default='127.0.0.1')
TEST_REDIS_PORT = config('TEST_REDIS_PORT', cast=int, default=6379)
TEST_REDIS_PASSWD = config('TEST_REDIS_PASSWD', default='')

DB_URI = config('DB_URI')
TEST_DB_URI = config('TEST_DB_URI')

LOG_LEVEL = config('LOG_LEVEL', default='DEBUG')
LOG_PATH = config('LOG_PATH')
INCLUDE_IN_SCHEMA = config('include_in_schema', cast=bool, default=True)

if CODE_ENV == 'test':
    REDIS_HOST = TEST_REDIS_HOST
    REDIS_PORT = TEST_REDIS_PORT
    REDIS_PASSWD = TEST_REDIS_PASSWD

    DB_URI = TEST_DB_URI

TORTOISE_ORM = {
    'connections': {'default': DB_URI},
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
