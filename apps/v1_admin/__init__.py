from fastapi import FastAPI

import config
from apps.libs.exception import register_exception
from apps.v1_admin.resources import register_routers

v1_admin_app: FastAPI = FastAPI(include_in_schema=config.include_in_schema)


def init_sub_app(app: FastAPI):
    """注册子app"""

    register_exception(v1_admin_app)
    register_routers(v1_admin_app)
    app.mount(path='/api/v1/admin', app=v1_admin_app, name='v1_admin_app')
