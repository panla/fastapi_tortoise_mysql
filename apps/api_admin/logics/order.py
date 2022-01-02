from tortoise.models import QuerySet

from apps.models import Order
from apps.api_admin.entities import FilterOrderParser

class OrderResolver:

    @classmethod
    def list_orders(cls, parser: FilterOrderParser) -> QuerySet:
        """search/filter orders"""

        query = Order.filter(is_delete=False)
        return query
