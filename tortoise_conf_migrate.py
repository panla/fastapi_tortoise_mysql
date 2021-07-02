import config

TORTOISE_ORM = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'database': config.DB_DATABASE,
                'host': config.DB_HOST,
                'password': config.DB_PASSWD,
                'port': config.DB_PORT,
                'user': config.DB_USER,
                'minisize': 1,
                'maxsize': config.DB_MAX_SIZE,
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
