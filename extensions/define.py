from pydantic import BaseModel
from pydantic.typing import NoneType


class StatusCode(object):
    success = 10000

    bad_request = 40000
    unauthorized = 40100
    forbidden = 40300
    not_found = 40400
    method_not_allowed = 40500
    not_acceptable = 40600
    request_timeout = 40800
    length_required = 41100
    entity_too_large = 41300
    request_uri_too_long = 41400
    validator_error = 42200
    locked = 42300
    header_fields_too_large = 43100

    server_error = 45000
    unknown_error = 45001


# don`t overwrite custom extension Exception and StatusCode 
# example, already had raise and catch 404, don`t define 404

middleware_codes = {
    405: {'status_code': StatusCode.method_not_allowed, 'message': 'METHOD_NOT_ALLOWED', 'data': None},
    406: {'status_code': StatusCode.not_acceptable, 'message': 'NOT_ACCEPTABLE', 'data': None},
    408: {'status_code': StatusCode.request_timeout, 'message': 'REQUEST_TIMEOUT', 'data': None},
    411: {'status_code': StatusCode.length_required, 'message': 'LENGTH_REQUIRED', 'data': None},
    413: {'status_code': StatusCode.entity_too_large, 'message': 'REQUEST_ENTITY_TOO_LARGE', 'data': None},
    414: {'status_code': StatusCode.request_uri_too_long, 'message': 'REQUEST_URI_TOO_LONG', 'data': None},
    431: {
        'status_code': StatusCode.header_fields_too_large,
        'message': 'REQUEST_HEADER_FIELDS_TOO_LARGE',
        'data': None
    },
}


class BadRequestSchema(BaseModel):
    status_code: int = StatusCode.bad_request
    message: str = ''
    data: NoneType = "null"


class UnauthorizedSchema(BaseModel):
    status_code: int = StatusCode.unauthorized
    message: str = ''
    data: NoneType = "null"


class ForbiddenSchema(BaseModel):
    status_code: int = StatusCode.forbidden
    message: str = ''
    data: NoneType = "null"


class NotFoundSchema(BaseModel):
    status_code: int = StatusCode.not_found
    message: str = ''
    data: NoneType = "null"


class ValidatorErrorSchema(BaseModel):
    status_code: int = StatusCode.validator_error
    message: str = ''
    data: NoneType = "null"


error_schema= {
    400: {
        'model': BadRequestSchema,
        'description': 'bad_request'
    },
    401: {
        'model': UnauthorizedSchema,
        'description': 'unauthorized'
    },
    403: {
        'model': ForbiddenSchema,
        'description': 'forbidden'
    },
    404: {
        'model': NotFoundSchema,
        'description': 'not_found'
    },
    422: {
        'model': ValidatorErrorSchema,
        'description': 'request parameters validator'
    }
}
