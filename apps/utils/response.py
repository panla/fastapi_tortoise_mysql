from typing import Any

from fastapi import HTTPException
from pydantic import BaseModel

from apps.utils.code import Code


class UnauthorizedException(HTTPException):
    pass


class ForbiddenException(HTTPException):
    pass


class NotFoundException(HTTPException):
    pass


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


class BadRequest(BaseModel):
    code: int = Code.http_error
    message: str = ''
    data: Any = None


class Unauthorized(BaseModel):
    code: int = Code.token_expired
    message: str = ''
    data: Any = None


class Forbidden(BaseModel):
    code: int = Code.forbidden
    message: str = ''
    data: Any = None


class NotFound(BaseModel):
    code: int = Code.no_found
    message: str = ''
    data: Any = None


class ValidatorError(BaseModel):
    code: int = Code.validator_error
    message: str = ''
    data: Any = None


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
