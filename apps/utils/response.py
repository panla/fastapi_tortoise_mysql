from fastapi import HTTPException
from pydantic import BaseModel

from apps.utils.code import Code


class UnauthorizedException(HTTPException):
    pass


class ForbiddenException(HTTPException):
    pass


class NotFoundException(HTTPException):
    pass


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


class Unauthorized(BaseModel):
    code: int = Code.token_expired
    message: str = ''


class Forbidden(BaseModel):
    code: int = Code.forbidden
    message: str = ''


class NotFound(BaseModel):
    code: int = Code.no_found
    message: str = ''


class ValidatorError(BaseModel):
    code: int = Code.validator_error
    message: str = ''


error_response = {
    400: {
        'model': BadRequest,
        'description': '请求错误'
    },
    401: {
        'model': Unauthorized,
        'description': 'TOKEN 验证失败'
    },
    403: {
        'model': Forbidden,
        'description': '无此权限'
    },
    404: {
        'model': NotFound,
        'description': '请求资源不存在'
    },
    422: {
        'model': ValidatorError,
        'description': '参数验证错误的返回值',
    }
}
