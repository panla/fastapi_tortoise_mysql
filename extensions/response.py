from typing import Optional, Any, Dict

from fastapi import Query
from extensions import logger
from pydantic import BaseModel
from pydantic.typing import NoneType

from conf.const import StatusCode, PaginateConst

# don`t overwrite custom extension Exception and StatusCode
# example, already had raised and catch 404, don`t define 404

middleware_code_contents = {
    405: {'code': StatusCode.method_not_allowed, 'message': 'METHOD_NOT_ALLOWED', 'data': None},
    406: {'code': StatusCode.not_acceptable, 'message': 'NOT_ACCEPTABLE', 'data': None},
    408: {'code': StatusCode.request_timeout, 'message': 'REQUEST_TIMEOUT', 'data': None},
    411: {'code': StatusCode.length_required, 'message': 'LENGTH_REQUIRED', 'data': None},
    413: {'code': StatusCode.entity_too_large, 'message': 'REQUEST_ENTITY_TOO_LARGE', 'data': None},
    414: {'code': StatusCode.request_uri_too_long, 'message': 'REQUEST_URI_TOO_LONG', 'data': None},
    431: {
        'code': StatusCode.header_fields_too_large,
        'message': 'REQUEST_HEADER_FIELDS_TOO_LARGE',
        'data': None
    }
}


class BadRequestSchema(BaseModel):
    code: int = StatusCode.bad_request
    message: str = ''
    data: NoneType = "null"


class UnauthorizedSchema(BaseModel):
    code: int = StatusCode.unauthorized
    message: str = ''
    data: NoneType = "null"


class ForbiddenSchema(BaseModel):
    code: int = StatusCode.forbidden
    message: str = ''
    data: NoneType = "null"


class NotFoundSchema(BaseModel):
    code: int = StatusCode.not_found
    message: str = ''
    data: NoneType = "null"


class ValidatorErrorSchema(BaseModel):
    code: int = StatusCode.validator_error
    message: str = ''
    data: NoneType = "null"


error_schema = {
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


def resp_success(message: str = '', print_msg: str = '', data: Any = None):
    if print_msg:
        pass
    else:
        if message and message != 'success':
            print_msg = message

    if print_msg:
        logger.info(print_msg)

    return {'message': message, 'data': data}


class SchemaMixin(BaseModel):
    code: int = 10000
    message: str = ''
    data: Optional[Any]

    @classmethod
    def ok(cls, data: Any = None) -> Dict[str, Any]:
        return cls(code=cls.code, message=cls.message, data=data).dict()


class NormalSchema(SchemaMixin):
    """"""

    data: Optional[str] = 'success'


class FilterParserMixin(BaseModel):
    """search list data"""

    page: Optional[int] = Query(PaginateConst.DefaultNum, title='page', gte=PaginateConst.MinNum)
    pagesize: Optional[int] = Query(PaginateConst.DefaultSize, title='pagesize', gte=1, lte=PaginateConst.MaxSize)
