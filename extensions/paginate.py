from tortoise.queryset import QuerySet, MODEL

from conf.const import PaginateConst


class Pagination(object):
    def __init__(
            self,
            query: QuerySet,
            page: int = PaginateConst.DefaultNum,
            pagesize: int = PaginateConst.DefaultSize
    ) -> None:
        self.query = query
        self.page = page
        self.pagesize = pagesize

    def items(self) -> QuerySet[MODEL]:
        return self.query.offset((self.page - 1) * self.pagesize).limit(self.pagesize)
