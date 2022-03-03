from tortoise.queryset import QuerySet, MODEL

from conf.const import PaginateConst


class Pagination(object):
    def __init__(
            self,
            query: QuerySet,
            page: int = PaginateConst.DefaultNum,
            page_size: int = PaginateConst.DefaultSize
    ) -> None:
        self.query = query
        self.page = page
        self.page_size = page_size

    def items(self) -> QuerySet[MODEL]:
        return self.query.offset((self.page - 1) * self.page_size).limit(self.page_size)
