from typing import Any

from fastapi import HTTPException
from pydantic import BaseModel

from apps.utils import StatusCode


class UnauthorizedException(HTTPException):
    pass


class ForbiddenException(HTTPException):
    pass


class NotFoundException(HTTPException):
    pass


class MethodNotAllowedException(HTTPException):
    pass


class BadRequest(BaseModel):
    status_code: int = StatusCode.http_error
    message: str = ''
    data: Any = None


class Unauthorized(BaseModel):
    status_code: int = StatusCode.token_expired
    message: str = ''
    data: Any = None


class Forbidden(BaseModel):
    status_code: int = StatusCode.forbidden
    message: str = ''
    data: Any = None


class NotFound(BaseModel):
    status_code: int = StatusCode.no_found
    message: str = ''
    data: Any = None


class ValidatorError(BaseModel):
    status_code: int = StatusCode.validator_error
    message: str = ''
    data: Any = None


def resp_success(message: str = '', data: Any = None):
    return {'status_code': 10000, 'message': message, 'data': data}


def raise_400(message: str):
    raise HTTPException(status_code=400, detail=message)


def raise_401(message: str):
    raise UnauthorizedException(status_code=401, detail=message)


def raise_403(message: str):
    raise ForbiddenException(status_code=403, detail=message)


def raise_404(message: str):
    raise NotFoundException(status_code=404, detail=message)


def raise_405(message: str):
    raise MethodNotAllowedException(status_code=405, detail=message)


error_response = {
    400: {
        'model': BadRequest,
        'description': '请求错误 data=null'
    },
    401: {
        'model': Unauthorized,
        'description': 'TOKEN 验证失败 data=null'
    },
    403: {
        'model': Forbidden,
        'description': '无此权限 data=null'
    },
    404: {
        'model': NotFound,
        'description': '请求资源不存在 data=null'
    },
    422: {
        'model': ValidatorError,
        'description': '参数验证错误的返回值 data=null',
    }
}
