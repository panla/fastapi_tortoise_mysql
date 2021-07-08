from apps.models import Order


def filter_orders(params: dict):
    """搜索订单"""

    query = Order.filter(is_delete=False)
    return query
