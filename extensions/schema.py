from typing import Optional, Any
from types import NoneType

from fastapi import Query
from pydantic import BaseModel

from conf.const import StatusCode, PaginateConst


class BadRequestSchema(BaseModel):
    code: int = StatusCode.BadRequest
    message: str = ''
    data: NoneType = 'null'


class UnauthorizedSchema(BaseModel):
    code: int = StatusCode.Unauthorized
    message: str = ''
    data: NoneType = 'null'


class ForbiddenSchema(BaseModel):
    code: int = StatusCode.Forbidden
    message: str = ''
    data: NoneType = 'null'


class NotFoundSchema(BaseModel):
    code: int = StatusCode.NotFound
    message: str = ''
    data: NoneType = 'null'


class ValidatorErrorSchema(BaseModel):
    code: int = StatusCode.ValidatorError
    message: str = ''
    data: NoneType = 'null'


ErrorSchema = {
    400: {
        'model': BadRequestSchema,
        'description': 'BadRequest'
    },
    401: {
        'model': UnauthorizedSchema,
        'description': 'Unauthorized'
    },
    403: {
        'model': ForbiddenSchema,
        'description': 'Forbidden'
    },
    404: {
        'model': NotFoundSchema,
        'description': 'NotFound'
    },
    422: {
        'model': ValidatorErrorSchema,
        'description': 'Request Parameters Validator'
    }
}



class SchemaMixin(BaseModel):
    code: int = StatusCode.Success
    message: str = 'success'
    data: Optional[Any]


class NormalSchema(SchemaMixin):
    """default normal common return schema"""

    data: Optional[str] = 'success'


class FilterParserMixin(BaseModel):
    """search list data"""

    page: Optional[int] = Query(PaginateConst.DefaultNum, title='page', gte=PaginateConst.MinNum)
    page_size: Optional[int] = Query(PaginateConst.DefaultSize, title='page_size', gte=1, lte=PaginateConst.MaxSize)
