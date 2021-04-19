from fastapi import FastAPI

from apps.libs.database import init_db
from apps.libs.exception import register_exception
from apps.libs.middleare import register_cross

from apps.libs.sub_app import v1_admin_app
from apps.resources.v1.admin import register_routers as register_v1_admin_routers


def init_router(app: FastAPI, function):
    """加载路由"""

    function(app)


def init_sub_app(app: FastAPI, sub_app: FastAPI, root_path: str, name: str, router_func):
    """注册子app"""

    register_exception(sub_app)
    register_cross(app)
    init_router(sub_app, router_func)
    app.mount(path=root_path, app=sub_app, name=name)


def init_app(app: FastAPI):
    """初始化app"""

    init_db(app)
    # register_exception(app)
    # register_cross(app)

    init_sub_app(app, v1_admin_app, '/api/v1/admin', 'v1_admin_app', register_v1_admin_routers)
