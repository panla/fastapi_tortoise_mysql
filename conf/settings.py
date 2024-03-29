from functools import lru_cache
from typing import Optional

from pydantic import BaseModel


class LogSetting(BaseModel):
    LEVEL: Optional[str] = 'DEBUG'
    PATH: str
    STDOUT: Optional[bool] = True
    ROTATION: Optional[str] = '00:00'
    RETENTION: Optional[str] = '30 days'
    COMPRESSION: Optional[str] = None


class ServiceSetting(BaseModel):
    # openapi swagger
    INCLUDE_IN_SCHEMA: Optional[bool] = True


class AuthenticSetting(BaseModel):
    ADMIN_SECRETS: str
    ADMIN_TOKEN_EXP_DELTA: Optional[int] = 864000


class RedisSetting(BaseModel):
    HOST: Optional[str] = '127.0.0.1'
    PORT: Optional[int] = 6379
    PASSWD: Optional[str] = None
    SOCKET_TIMEOUT: Optional[float] = 10
    SOCKET_CONNECT_TIMEOUT: Optional[float] = 10
    MAX_CONNECTIONS: Optional[int] = None
    USER: Optional[str] = None


class DBSetting(BaseModel):
    POOL_RECYCLE: Optional[int] = 1000

    USER: Optional[str] = 'root'
    PASSWD: str
    HOST: Optional[str] = '127.0.0.1'
    PORT: Optional[int] = 3306
    DATABASE: str
    MAX_SIZE: Optional[int] = 5


class Setting(BaseModel):
    log: LogSetting
    service: ServiceSetting
    authentic: AuthenticSetting
    redis: RedisSetting
    db: DBSetting


class ORMSetting:
    def __init__(self, db: DBSetting):
        self.db = db

    def _base_orm_conf(self, apps: dict) -> dict:
        return {
            'connections': {
                'default': {
                    'engine': 'tortoise.backends.mysql',
                    'credentials': {
                        'host': self.db.HOST,
                        'port': self.db.PORT,
                        'user': self.db.USER,
                        'password': self.db.PASSWD,
                        'database': self.db.DATABASE,
                        'minsize': 1,
                        'maxsize': self.db.MAX_SIZE,
                        'charset': 'utf8mb4',
                        'pool_recycle': self.db.POOL_RECYCLE
                    }
                }
            },
            'apps': apps,
            'use_tz': False,
            'timezone': 'Asia/Shanghai'
        }

    @property
    @lru_cache
    def orm_link_conf(self) -> dict:
        orm_apps_settings = {
            'models': {
                'models': [
                    'aerich.models',
                    'apps.models.models'
                ],
                'default_connection': 'default',
            }
        }
        return self._base_orm_conf(orm_apps_settings)

    @property
    def orm_migrate_conf(self) -> dict:
        orm_apps_settings = {
            'models': {
                'models': [
                    'aerich.models',
                    'apps.models.models'
                ],
                'default_connection': 'default',
            }
        }
        return self._base_orm_conf(orm_apps_settings)

    @property
    def orm_test_migrate_conf(self) -> dict:
        orm_apps_settings = {
            'models': {
                'models': [
                    'aerich.models',
                    'apps.models.models'
                ],
                'default_connection': 'default',
            }
        }
        return self._base_orm_conf(orm_apps_settings)
