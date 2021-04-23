from fastapi import APIRouter

from apps.extension.route import Route
from apps.models import Order
from apps.entities.v1.admin.order import ListOrderSchema
from apps.entities.v1.admin.order import read_exclude, read_computed
from apps.utils.response import error_response

router = APIRouter(route_class=Route)


@router.get('', response_model=ListOrderSchema, status_code=200, responses=error_response)
async def list_orders():

    query = Order.all()
    orders = Order.QuerySetCreator(exclude=read_exclude, computed=read_computed).from_queryset(query)

    total = await query.count()
    orders = await orders
    orders = orders.dict().get('__root__')
    return {'total': total, 'orders': orders}
