from config import DefaultPageNum, DefaultPageSize

from tortoise.queryset import QuerySet


class Pagination(object):
    def __init__(self, query: QuerySet, page: int = DefaultPageNum, pagesize: int = DefaultPageSize) -> None:
        self.query = query
        self.page = page
        self.pagesize = pagesize

    def items(self) -> QuerySet:
        return self.query.offset((self.page - 1) * self.pagesize).limit(self.pagesize)
