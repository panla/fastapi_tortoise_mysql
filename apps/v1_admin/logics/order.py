from apps.models import Order


def filter_orders(params: dict):
    """搜索订单"""

    query = Order.filter(is_delete=False)
    return query


async def response_orders(orders):
    """组合订单列表返回数据"""

    _orders = []
    for order in orders:
        _order = order.to_dict(selects=['id', 'amount', 'remarks', 'created_time'])
        _order['owner'] = await order.owner
        _orders.append(_order)
    return _orders
