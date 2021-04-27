from fastapi import APIRouter, Depends

from apps.models import Order
from apps.utils import error_response
from apps.extension.route import Route
from apps.entities.v1.admin.order import ListOrderSchema
from apps.entities.v1.admin.order import read_exclude, read_computed
from apps.entities.v1.admin.order import filter_params

router = APIRouter(route_class=Route)


@router.get('', response_model=ListOrderSchema, status_code=200, responses=error_response)
async def list_orders(params: dict = Depends(filter_params)):

    query = Order.all()
    total = await query.count()

    query = Order.paginate(query, params['page'], params['pagesize'] or total)
    orders = await Order.QuerySetCreator(exclude=read_exclude, computed=read_computed).from_queryset(query)

    orders = orders.dict().get('__root__')
    return {'total': total, 'orders': orders}
