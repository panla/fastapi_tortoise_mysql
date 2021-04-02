import os
import logging
import traceback
from logging.handlers import TimedRotatingFileHandler

from fastapi import FastAPI
from fastapi import Request, status
from fastapi.logger import logger
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse
from tortoise.contrib.fastapi import register_tortoise

import config
from apps.resources import register_routers


def init_app(app: FastAPI):
    set_logger_handle(app)
    init_db(app)
    init_router(app)
    register_middleware(app)


def init_db(app: FastAPI):
    """绑定 tortoise-orm"""

    register_tortoise(
        app,
        config=config.TORTOISE_ORM
    )


def init_router(app):
    """加载路由"""
    register_routers(app)


def set_logger_handle(app: FastAPI):
    """配置 logger handle"""

    log_level = config.LOG_LEVEL.upper()
    logfile_path = config.LOG_PATH

    os.makedirs(os.path.dirname(logfile_path), exist_ok=True)

    file_handler = TimedRotatingFileHandler(logfile_path, 'midnight')
    file_handler.setLevel(level=log_level)
    file_handler.setFormatter(
        logging.Formatter('[%(asctime)s>] [%(levelname)s] <-%(filename)s-line %(lineno)d>  %(message)s')
    )
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    app.logger = logger


def register_middleware(app: FastAPI):
    """解决跨域"""

    app.add_middleware(
        CORSMiddleware,
        allow_origin_regex='https?://.*',
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )


def register_exception(app: FastAPI):

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """捕获参数验证错误"""

        exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
        log_message(request, exc_str)
        # content = exc.errors()
        content = {'code': status.HTTP_422_UNPROCESSABLE_ENTITY, 'data': None, 'message': exc_str}
        return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        """捕获HTTPException"""

        log_message(request, exc.detail)
        content = {'code': exc.status_code, 'data': None, 'message': exc.detail}
        return JSONResponse(content=content, status_code=exc.status_code)

    @app.exception_handler(Exception)
    async def exception_handle(request: Request, exc: Exception):
        """捕获其他异常"""

        log_message(request, traceback.format_exc())
        content = {'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'data': None, 'message': str(exc)}
        return JSONResponse(content=content, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


def log_message(request: Request, e):
    """打印 error 时的日志"""

    _logger = request.app.logger
    _logger.error('start error'.center(60, '*'))
    _logger.error(f'{request.method} {request.url}')
    _logger.error(f'error is {e}')
    _logger.error('end error'.center(60, '*'))
