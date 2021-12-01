from typing import List
from functools import lru_cache

from pydantic import BaseModel


class LogConfig(BaseModel):
    LOG_LEVEL: str = 'DEBUG'
    LOG_PATH: str


class ServiceConfig(BaseModel):
    # openapi swagger
    INCLUDE_IN_SCHEMA: bool = True

    # socket.io on
    SOCKET_IO_ON: bool = False


class AuthenticConfig(BaseModel):
    ADMIN_SECRETS: str
    ADMIN_TOKEN_EXP_DELTA: int = 864000


class SocketIOConfig(BaseModel):
    SOCKET_IO_NAMESPACES: List[str] = ['/']
    SOCKET_IO_PATH: str = 'socket.io'
    SOCKET_IO_MOUNT: str = '/'


class RedisConfig(BaseModel):
    REDIS_HOST: str = '127.0.0.1'
    REDIS_PORT: int = 6379
    REDIS_PASSWD: str = ''


class DBConfig(BaseModel):
    DB_POOL_RECYCLE: str = 1000

    DB_USER: str = 'root'
    DB_PASSWD: str
    DB_HOST: str = '127.0.0.1'
    DB_PORT: int = 3306
    DB_DATABASE: str
    DB_MAX_SIZE: int = 5


class DBSetting():
    def __init__(self, db):
        self.db = db

    def _base_orm_conf(self, apps: dict) -> dict:
        return {
            'connections': {
                'default': {
                    'engine': 'tortoise.backends.mysql',
                    'credentials': {
                        'host': self.db.DB_HOST,
                        'port': self.db.DB_PORT,
                        'user': self.db.DB_USER,
                        'password': self.db.DB_PASSWD,
                        'database': self.db.DB_DATABASE,
                        'minsize': 1,
                        'maxsize': self.db.DB_MAX_SIZE,
                        'charset': 'utf8mb4',
                        'pool_recycle': self.db.DB_POOL_RECYCLE
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
