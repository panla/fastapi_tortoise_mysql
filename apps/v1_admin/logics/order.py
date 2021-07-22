from apps.models import Order


def filter_orders(params: dict):
    """search/filter orders"""

    query = Order.filter(is_delete=False)
    return query
