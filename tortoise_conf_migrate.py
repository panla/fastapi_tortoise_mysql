from config import Config

TORTOISE_ORM = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'database': Config.DB_DATABASE,
                'host': Config.DB_HOST,
                'password': Config.DB_PASSWD,
                'port': Config.DB_PORT,
                'user': Config.DB_USER,
                'minsize': 1,
                'maxsize': Config.DB_MAX_SIZE,
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
