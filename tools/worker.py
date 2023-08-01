"""
extend gunicorn worker_class, if had installed uvloop httptools, use them
"""

from uvicorn.workers import UvicornWorker

try:
    import uvloop
    import httptools


    class Worker(UvicornWorker):
        CONFIG_KWARGS = {'loop': 'uvloop', 'http': 'httptools'}


    del httptools
    del uvloop
except ImportError:
    class Worker(UvicornWorker):
        CONFIG_KWARGS = {'loop': 'asyncio', 'http': 'auto'}
