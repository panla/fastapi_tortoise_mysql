import config

TORTOISE_ORM = {
    'connections': {'default': config.MYSQL_URI},
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
