from typing import Optional, Any

from fastapi import Query
from pydantic import BaseModel

from config import DefaultPageSize, DefaultPageNum, MaxPageSize, MinPageNum


class SchemaMixin(BaseModel):

    code: int = 10000
    message: str = ''
    data: Optional[Any]


class FilterParserMixin(BaseModel):

    page: Optional[int] = Query(default=DefaultPageNum, description='page', gte=MinPageNum)
    pagesize: Optional[int] = Query(default=DefaultPageSize, description='pagesize', gte=1, lte=MaxPageSize)
