import traceback

from fastapi import FastAPI
from fastapi import Request, status
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse


def log_message(request: Request, e):
    """打印 error 时的日志"""

    _logger = request.app.logger
    _logger.error('start error'.center(60, '*'))
    _logger.error(f'{request.method} {request.url}')
    _logger.error(f'error is {e}')
    _logger.error('end error'.center(60, '*'))


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
