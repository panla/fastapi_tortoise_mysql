"""
扩展 gunicorn worker_class 如果安装 uvloop httptols 的话，指明用上
"""

from uvicorn.workers import UvicornWorker

try:
    import uvloop
    import httptools


    class Worker(UvicornWorker):
        CONFIG_KWARGS = {"loop": "uvloop", "http": "httptools"}
except ImportError:
    class Worker(UvicornWorker):
        CONFIG_KWARGS = {"loop": "asyncio", "http": "auto"}
