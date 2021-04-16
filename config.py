from starlette.config import Config

config = Config('.env')

CODE_ENV = config('CODE_ENV', default='dev')

PRD_REDIS_HOST = config('REDIS_HOST', default='127.0.0.1')
PRD_REDIS_PORT = config('PRD_REDIS_PORT', cast=int, default=6379)
PRD_REDIS_DB = config('PRD_REDIS_DB', cast=int, default=0)
PRD_REDIS_USER = config('PRD_REDIS_USER', default=None)
PRD_REDIS_PASSWD = config('PRD_REDIS_PASSWD', default=None)

DEV_REDIS_HOST = config('DEV_REDIS_HOST', default='127.0.0.1')
DEV_REDIS_PORT = config('DEV_REDIS_PORT', cast=int, default=6379)
DEV_REDIS_DB = config('DEV_REDIS_DB', cast=int, default=0)
DEV_REDIS_USER = config('DEV_REDIS_USER', default=None)
DEV_REDIS_PASSWD = config('DEV_REDIS_PASSWD', default=None)

TEST_REDIS_HOST = config('TEST_REDIS_HOST', default='127.0.0.1')
TEST_REDIS_PORT = config('TEST_REDIS_PORT', cast=int, default=6379)
TEST_REDIS_DB = config('TEST_REDIS_DB', cast=int, default=0)
TEST_REDIS_USER = config('TEST_REDIS_USER', default=None)
TEST_REDIS_PASSWD = config('TEST_REDIS_PASSWD', default=None)

PRD_MYSQL_URI = config('PRD_MYSQL_URI')
DEV_MYSQL_URI = config('DEV_MYSQL_URI')
TEST_MYSQL_URI = config('TEST_MYSQL_URI')

LOG_LEVEL = config('LOG_LEVEL', default='DEBUG')
LOG_PATH = config('LOG_PATH')

if CODE_ENV == 'prd':
    REDIS_HOST = PRD_REDIS_HOST
    REDIS_PORT = PRD_REDIS_PORT
    REDIS_DB = PRD_REDIS_DB
    REDIS_USER = PRD_REDIS_USER
    REDIS_PASSWD = PRD_REDIS_PASSWD

    MYSQL_URI = PRD_MYSQL_URI

    include_in_schema = False
elif CODE_ENV == 'test':
    REDIS_HOST = TEST_REDIS_HOST
    REDIS_PORT = TEST_REDIS_PORT
    REDIS_DB = TEST_REDIS_DB
    REDIS_USER = TEST_REDIS_USER
    REDIS_PASSWD = TEST_REDIS_PASSWD

    MYSQL_URI = TEST_MYSQL_URI

    include_in_schema = True
else:
    REDIS_HOST = DEV_REDIS_HOST
    REDIS_PORT = DEV_REDIS_PORT
    REDIS_DB = DEV_REDIS_DB
    REDIS_USER = DEV_REDIS_USER
    REDIS_PASSWD = DEV_REDIS_PASSWD

    MYSQL_URI = DEV_MYSQL_URI

    include_in_schema = True

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
