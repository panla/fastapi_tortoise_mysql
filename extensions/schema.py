from typing import Optional, Any

from fastapi import Query
from pydantic import BaseModel
from pydantic.typing import NoneType

from conf.const import StatusCode, PaginateConst


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


ErrorSchema = {
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


class SchemaMixin(BaseModel):
    code: int = 10000
    message: str = ''
    data: Optional[Any]


class NormalSchema(SchemaMixin):
    """"""

    data: Optional[str] = 'success'


class FilterParserMixin(BaseModel):
    """search list data"""

    page: Optional[int] = Query(PaginateConst.DefaultNum, title='page', gte=PaginateConst.MinNum)
    pagesize: Optional[int] = Query(PaginateConst.DefaultSize, title='pagesize', gte=1, lte=PaginateConst.MaxSize)
