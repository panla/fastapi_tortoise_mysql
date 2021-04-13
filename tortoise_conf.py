import config


TORTOISE_ORM = {
    "connections": {"default": config.MYSQL_URI},
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
