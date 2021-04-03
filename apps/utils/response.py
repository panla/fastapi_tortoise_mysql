from typing import Any

from fastapi.responses import JSONResponse
from pydantic import BaseModel

from apps.utils.code import Code


def response(status_code: 200, code: 10000, data: Any, message: ''):
    content = {'code': code, 'message': message, 'data': data}
    return JSONResponse(content=content, status_code=status_code)


def resp_200(data: Any = None, message: str = ''):
    return {'code': Code.success, 'message': message, 'data': data}


def resp_201(data: Any = None, message: str = ''):
    return {'code': Code.success, 'message': message, 'data': data}


def resp_400(message: str):
    return {'code': Code.http_error, 'data': None, 'message': message}


def resp_404(message: str):
    return {'code': Code.no_exists, 'data': None, 'message': message}


class ValidatorError(BaseModel):
    code: int = 10003
    message: str = ''
    data: Any = None


error_response = {
    422: {
        'model': ValidatorError,
        'description': '参数验证错误的返回值，data=null',
    }
}
