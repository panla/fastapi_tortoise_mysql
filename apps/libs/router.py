from fastapi import FastAPI

from apps.resources import register_routers


def init_router(app: FastAPI):
    """加载路由"""

    register_routers(app)
