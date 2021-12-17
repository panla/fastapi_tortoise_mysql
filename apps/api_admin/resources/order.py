from fastapi import APIRouter, Depends

from extensions import Route, Pagination, error_schema, resp_success
from apps.api_admin.entities import (
    ListOrderSchema, FilterCarParser
)
from apps.api_admin.logics import OrderResolver

router = APIRouter(route_class=Route, responses=error_schema)


@router.get('', response_model=ListOrderSchema, status_code=200)
async def list_orders(
        parser: FilterCarParser = Depends(FilterCarParser)
):
    """the api of read list orders"""

    payload = parser.dict()

    query = OrderResolver.list_orders(payload)
    total = await query.count()
    query = Pagination(query, payload['page'], payload['pagesize'] or total).items()
    orders = await query.prefetch_related('owner')

    return resp_success(data={'total': total, 'orders': orders})
