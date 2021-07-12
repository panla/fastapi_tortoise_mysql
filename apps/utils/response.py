__all__ = [
    'resp_success', 'error_response',
]

from typing import Any

from pydantic import BaseModel

from apps.utils import StatusCode, logger


class BadRequestSchema(BaseModel):
    status_code: int = StatusCode.bad_request
    message: str = ''
    data: Any = None


class UnauthorizedSchema(BaseModel):
    status_code: int = StatusCode.bad_request
    message: str = ''
    data: Any = None


class ForbiddenSchema(BaseModel):
    status_code: int = StatusCode.forbidden
    message: str = ''
    data: Any = None


class NotFoundSchema(BaseModel):
    status_code: int = StatusCode.not_found
    message: str = ''
    data: Any = None


class ValidatorErrorSchema(BaseModel):
    status_code: int = StatusCode.validator_error
    message: str = ''
    data: Any = None


def resp_success(message: str = '', data: Any = None):
    if message and message != 'success':
        logger.info(message)
    return {'status_code': 10000, 'message': message, 'data': data}


error_response = {
    400: {
        'model': BadRequestSchema,
        'description': '请求错误 data=null'
    },
    401: {
        'model': UnauthorizedSchema,
        'description': 'TOKEN 验证失败 data=null'
    },
    403: {
        'model': ForbiddenSchema,
        'description': '无此权限 data=null'
    },
    404: {
        'model': NotFoundSchema,
        'description': '请求资源不存在 data=null'
    },
    422: {
        'model': ValidatorErrorSchema,
        'description': '参数验证错误的返回值 data=null',
    }
}
