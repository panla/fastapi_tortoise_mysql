__all__ = [
    'StatusCode', 'middleware_codes', 'error_response',
]

from typing import Any

from pydantic import BaseModel


class StatusCode(object):
    success = 10000

    bad_request = 40000
    unauthorized = 400100
    forbidden = 40300
    not_found = 40400

    method_not_allowed = 40500
    request_timeout = 40800
    length_required = 41100
    entity_too_large = 41300
    request_uri_too_long = 41400
    validator_error = 42200
    header_fields_too_large = 43100

    server_error = 45000
    unknown_error = 45001


# 不要和自定义的异常冲突，会覆盖自定义抛出的异常
# 比如，已经自己抛出了 404，就不要在这里定义 404

middleware_codes = {
    405: {'status_code': StatusCode.method_not_allowed, 'message': 'METHOD_NOT_ALLOWED', 'data': None},
    408: {'status_code': StatusCode.entity_too_large, 'message': 'REQUEST_TIMEOUT', 'data': None},
    411: {'status_code': StatusCode.entity_too_large, 'message': 'LENGTH_REQUIRED', 'data': None},
    413: {'status_code': StatusCode.entity_too_large, 'message': 'REQUEST_ENTITY_TOO_LARGE', 'data': None},
    414: {'status_code': StatusCode.entity_too_large, 'message': 'REQUEST_URI_TOO_LONG', 'data': None},
    432: {'status_code': StatusCode.entity_too_large, 'message': 'REQUEST_HEADER_FIELDS_TOO_LARGE', 'data': None},
}


class BadRequestSchema(BaseModel):
    status_code: int = StatusCode.bad_request
    message: str = ''
    data: Any = None


class UnauthorizedSchema(BaseModel):
    status_code: int = StatusCode.unauthorized
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
