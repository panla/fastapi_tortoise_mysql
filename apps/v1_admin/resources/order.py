from fastapi import APIRouter, Depends

from apps.extensions import Route, error_response
from apps.utils import resp_success
from apps.models import Order, AdminUser
from apps.modules import get_current_admin_user
from apps.v1_admin.entities import ListOrderSchema
from apps.v1_admin.entities import filter_order_dependency
from apps.v1_admin.logics import filter_orders

router = APIRouter(route_class=Route)


@router.get('', response_model=ListOrderSchema, status_code=200, responses=error_response)
async def list_orders(
    params: dict = Depends(filter_order_dependency),
    admin_user: AdminUser = Depends(get_current_admin_user)
):

    query = filter_orders(params)
    query =query.prefetch_related('owner')
    total = await query.count()

    query = await Order.paginate(query, params['page'], params['pagesize'] or total)
    return resp_success(data={'total': total, 'orders': query})
