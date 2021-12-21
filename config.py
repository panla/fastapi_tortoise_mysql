__all__ = [
    'Config', 'ORM_LINK_CONF', 'ORM_MIGRATE_CONF', 'ORM_TEST_MIGRATE_CONF'
]

import os
from pathlib import Path
from functools import lru_cache

import pytomlpp
from pydantic import BaseModel

from conf.settings import (
    LogSetting, ServiceSetting, AuthenticSetting, RedisSetting, DBSetting, ORMSetting
)

BASE_DIR = Path(__file__).absolute().parent


class Setting(BaseModel):
    log: LogSetting
    service: ServiceSetting
    authentic: AuthenticSetting
    redis: RedisSetting
    db: DBSetting


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

ORM_LINK_CONF = ORMSetting(Config.db).orm_link_conf
ORM_MIGRATE_CONF = ORMSetting(Config.db).orm_migrate_conf
ORM_TEST_MIGRATE_CONF = ORMSetting(Config.db).orm_test_migrate_conf

LogConfig = Config.log
ServiceConfig = Config.service
AuthenticConfig = Config.authentic
RedisConfig = Config.redis

DefaultPageNum = 1
DefaultPageSize = 10
MaxPageSize = 40
MinPageNum = 1
