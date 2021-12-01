__all__ = [
    'Config', 'ORM_LINK_CONF', 'ORM_MIGRATE_CONF', 'ORM_TEST_MIGRATE_CONF'
]

import os
from pathlib import Path
from functools import lru_cache

import pytomlpp
from pydantic import BaseModel

from conf.settings import LogConfig, ServiceConfig, AuthenticConfig, SocketIOConfig, RedisConfig, DBConfig, DBSetting


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Setting(BaseModel):
    log: LogConfig
    service: ServiceConfig
    authentic: AuthenticConfig
    socket_io: SocketIOConfig
    redis: RedisConfig
    db: DBConfig


@lru_cache()
def get_settings() -> Setting:
    CODE_ENV = os.environ.get('CODE_ENV', 'prd')

    if CODE_ENV == 'test':
        p = Path(BASE_DIR).joinpath('conf/test.local.toml')
    else:
        p = Path(BASE_DIR).joinpath('conf/product.local.toml')

    if not p.is_file():
        raise Exception('config no exists')

    settings = Setting.parse_obj(pytomlpp.load(p))
    return settings


Config = get_settings()

ORM_LINK_CONF = DBSetting(Config.db).orm_link_conf
ORM_MIGRATE_CONF = DBSetting(Config.db).orm_migrate_conf
ORM_TEST_MIGRATE_CONF = DBSetting(Config.db).orm_test_migrate_conf
