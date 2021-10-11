from tortoise.models import QuerySet

from apps.models import Order


class OrderResolver:
    
    @classmethod
    def list_orders(cls, params: dict) -> QuerySet:
        """search/filter orders"""

        query = Order.filter(is_delete=False)
        return query
