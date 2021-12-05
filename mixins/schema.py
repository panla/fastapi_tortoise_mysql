from typing import Optional, Any

from fastapi import Query
from pydantic import BaseModel


class SchemaMixin(BaseModel):

    code: int = 10000
    message: str = ''
    data: Optional[Any]


class FilterParserMixin(BaseModel):

    page: Optional[int] = Query(default=1, description='page', gte=1)
    pagesize: Optional[int] = Query(default=10, description='pagesize', gte=1, lte=40)
