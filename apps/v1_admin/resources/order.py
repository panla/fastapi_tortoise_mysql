from fastapi import APIRouter, Depends

from extensions import Route, error_response, resp_success, Pagination
from apps.models import AdminUser
from apps.modules import get_current_admin_user
from apps.v1_admin.entities import (
    ListOrderSchema, FilterCarParser
)
from apps.v1_admin.logics import filter_orders

router = APIRouter(route_class=Route, responses=error_response)


@router.get('', response_model=ListOrderSchema, status_code=200)
async def list_orders(
        parser: FilterCarParser = Depends(FilterCarParser),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """the api of read list orders"""

    params = parser.dict()
    query = filter_orders(params)
    total = await query.count()
    result = Pagination(query, params['page'], params['pagesize'] or total).result()
    orders = await query.prefetch_related('owner')

    return resp_success(data={'total': total, 'orders': orders})
