from tortoise.models import QuerySet

from extensions import Pagination
from apps.models import Order
from apps.api_admin.schemas import FilterOrderParser


class OrderResolver:

    @classmethod
    async def list_orders(cls, parser: FilterOrderParser) -> dict:
        """search/filter orders"""

        query = Order.filter(is_delete=False)

        total = await query.count()
        query = Pagination(query, parser.page, parser.page_size or total).items()
        orders = await query.prefetch_related('owner')

        return {'total': total, 'orders': orders}
