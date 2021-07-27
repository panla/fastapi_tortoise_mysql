from tortoise.models import QuerySet

from apps.models import Order


def filter_orders(params: dict) -> QuerySet:
    """search/filter orders"""

    query = Order.filter(is_delete=False)
    return query
