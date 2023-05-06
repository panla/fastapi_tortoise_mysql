import traceback
from typing import Union, Any

from fastapi import FastAPI, Request, status
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse
from starlette.datastructures import URL
from tortoise.validators import ValidationError

from conf.const import StatusCode
from extensions.log import logger
from extensions.exceptions import BaseHTTPException


def log_message(method: str, url: Union[str, URL], message: Any):
    """log message when catch exception"""

    logger.error('start error, this is'.center(60, '*'))
    logger.error(f'{method} {url}')
    logger.error(message)
    logger.error('end error'.center(60, '*'))


def register_exception(app: FastAPI):
    @app.exception_handler(BaseHTTPException)
    async def catch_c_http_exception(request: Request, exc: BaseHTTPException):
        """catch custom exception"""

        log_message(request.method, request.url, exc.message)
        content = exc.response()
        return JSONResponse(content=content, status_code=exc.status_code, headers=exc.headers)

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        """catch FastAPI HTTPException"""

        log_message(request.method, request.url, exc.detail)
        content = {'code': StatusCode.BadRequest, 'message': exc.detail, 'data': None}
        return JSONResponse(content=content, status_code=exc.status_code, headers=exc.headers)

    @app.exception_handler(AssertionError)
    async def assert_exception_handle(request: Request, exc: AssertionError):
        """catch Python AssertError"""

        exc_str = ' '.join(exc.args)
        log_message(request.method, request.url, exc_str)
        content = {'code': StatusCode.AssertValidatorError, 'message': exc_str, 'data': None}
        return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @app.exception_handler(ValidationError)
    async def db_validation_exception_handle(request: Request, exc: ValidationError):
        """catch tortoise-orm ValidatorError"""

        exc_str = '|'.join(exc.args)
        log_message(request.method, request.url, exc.args)
        content = {'code': StatusCode.ValidatorError, 'message': exc_str, 'data': None}
        return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """catch FastAPI RequestValidationError"""

        exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
        log_message(request.method, request.url, exc)
        # content = exc.errors()
        content = {'code': StatusCode.RequestValidatorError, 'message': exc_str, 'data': None}
        return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @app.exception_handler(Exception)
    async def exception_handle(request: Request, exc: Exception):
        """catch other exception"""

        log_message(request.method, request.url, traceback.format_exc())
        content = {'code': StatusCode.ServerError, 'message': str(exc), 'data': None}
        return JSONResponse(content=content, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
