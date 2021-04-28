from fastapi import FastAPI

from apps.libs.database import init_db
from apps.libs.middleare import register_cross

from apps.v1_admin import init_sub_app as init_v1_admin_app


def init_app(app: FastAPI):
    """初始化app"""

    init_db(app)
    register_cross(app)

    init_v1_admin_app(app)
