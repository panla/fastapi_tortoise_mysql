MYSQL_URI = 'mysql://root:passwd@127.0.0.1:3306/ftm_test'


TORTOISE_ORM = {
    "connections": {"default": MYSQL_URI},
    "apps": {
        "models": {
            "models": [
                "aerich.models",
                "apps.models.__init__"
            ],
            "default_connection": "default",
        },
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}
