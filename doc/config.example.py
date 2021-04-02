#####################################################################
# redis

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_USER = None
REDIS_PASSWD = None

#####################################################################
# database

MYSQL_URI = "mysql://root:passwd@127.0.0.1:3306/db_name"

TORTOISE_ORM = {
    "connections": {"default": MYSQL_URI},
    "apps": {
        "models": {
            "models": [
                "apps.models.car",
                "apps.models.book",
                "aerich.models"
            ],
            "default_connection": "default",
        },
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}

#####################################################################
# log

LOG_LEVEL = 'DEBUG'
LOG_PATH = '/xxxx/fastapi_tortoise_mysql/logs/x.log'
