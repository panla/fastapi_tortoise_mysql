from typing import Optional, Any

from fastapi import Query
from pydantic import BaseModel

from conf.const import PaginateConst


class SchemaMixin(BaseModel):

    code: int = 10000
    message: str = ''
    data: Optional[Any]


class FilterParserMixin(BaseModel):

    page: Optional[int] = Query(PaginateConst.DefaultNum, title='page', gte=PaginateConst.MinNum)
    pagesize: Optional[int] = Query(PaginateConst.DefaultSize, title='pagesize', gte=1, lte=PaginateConst.MaxSize)
