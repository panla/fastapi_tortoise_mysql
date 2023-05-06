__all__ = [
    'BASE_DIR',
    'Config',
    'ORM_LINK_CONF',
    'ORM_MIGRATE_CONF',
    'ORM_TEST_MIGRATE_CONF',
    'LogConfig',
    'ServiceConfig',
    'AuthenticConfig',
    'RedisConfig'
]

import os
from pathlib import Path
from functools import lru_cache

import pytomlpp

from conf.const import EnvConst
from conf.settings import (
    Setting, ORMSetting
)

BASE_DIR = Path(__file__).absolute().parent


@lru_cache()
def get_settings() -> Setting:
    code_env = os.environ.get('CODE_ENV', EnvConst.PRD)

    if code_env == EnvConst.TEST:
        p = Path(BASE_DIR).joinpath('conf/test.local.toml')
        if not p.is_file():
            p = Path(BASE_DIR).joinpath('conf/test.toml')
    else:
        p = Path(BASE_DIR).joinpath('conf/product.local.toml')
        if not p.is_file():
            p = Path(BASE_DIR).joinpath('conf/product.toml')

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
