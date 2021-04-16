from typing import Any

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from apps.utils.code import Code


class UnauthorizedException(HTTPException):
    pass


class NotFoundException(HTTPException):
    pass


def response(status_code: 200, code: 10000, data: Any, message: ''):
    content = {'code': code, 'message': message, 'data': data}
    return JSONResponse(content=content, status_code=status_code)


def resp_200(data: Any = None, message: str = ''):
    return {'code': Code.success, 'message': message, 'data': data}


def resp_201(data: Any = None, message: str = ''):
    return {'code': Code.success, 'message': message, 'data': data}


def resp_400(message: str):
    raise HTTPException(status_code=400, detail=message)


def resp_401(message: str):
    raise UnauthorizedException(status_code=401, detail=message)


def resp_403(message: str):
    raise HTTPException(status_code=401, detail=message)


def resp_404(message: str):
    raise NotFoundException(status_code=404, detail=message)


class BadRequest(BaseModel):
    code: int = Code.http_error
    message: str = ''
    data: Any = None


class Unauthorized(BaseModel):
    code: int = Code.token_expired
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
        'description': '请求错误'
    },
    401: {
        'model': Unauthorized,
        'description': 'TOKEN 验证失败'
    },
    404: {
        'model': NotFound,
        'description': '请求资源不存在'
    },
    422: {
        'model': ValidatorError,
        'description': '参数验证错误的返回值，data=null',
    }
}
