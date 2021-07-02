DB_USER = 'root'
DB_PASSWD = 'passwd'
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_DATABASE = 'ftm_prd'
DB_MAX_SIZE = 5

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
