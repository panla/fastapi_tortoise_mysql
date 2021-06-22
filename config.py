from starlette.config import Config

config = Config('.env')

CODE_ENV = config('CODE_ENV', default='prd')

PRD_REDIS_HOST = config('REDIS_HOST', default='127.0.0.1')
PRD_REDIS_PORT = config('PRD_REDIS_PORT', cast=int, default=6379)
PRD_REDIS_DB = config('PRD_REDIS_DB', cast=int, default=0)
PRD_REDIS_PASSWD = config('PRD_REDIS_PASSWD', default='')

TEST_REDIS_HOST = config('TEST_REDIS_HOST', default='127.0.0.1')
TEST_REDIS_PORT = config('TEST_REDIS_PORT', cast=int, default=6379)
TEST_REDIS_DB = config('TEST_REDIS_DB', cast=int, default=0)
TEST_REDIS_PASSWD = config('TEST_REDIS_PASSWD', default='')

PRD_DB_URI = config('PRD_DB_URI')
TEST_DB_URI = config('TEST_DB_URI')

LOG_LEVEL = config('LOG_LEVEL', default='DEBUG')
LOG_PATH = config('LOG_PATH')
INCLUDE_IN_SCHEMA = config('include_in_schema', cast=bool, default=True)

if CODE_ENV == 'test':
    REDIS_HOST = TEST_REDIS_HOST
    REDIS_PORT = TEST_REDIS_PORT
    REDIS_DB = TEST_REDIS_DB
    REDIS_PASSWD = TEST_REDIS_PASSWD

    MYSQL_URI = TEST_DB_URI

else:
    REDIS_HOST = PRD_REDIS_HOST
    REDIS_PORT = PRD_REDIS_PORT
    REDIS_DB = PRD_REDIS_DB
    REDIS_PASSWD = PRD_REDIS_PASSWD

    MYSQL_URI = PRD_DB_URI

TORTOISE_ORM = {
    'connections': {'default': MYSQL_URI},
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
