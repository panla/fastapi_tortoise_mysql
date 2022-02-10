from fastapi import APIRouter, Depends

from extensions import Route, Pagination, ErrorSchema
from apps.api_admin.schemas import (
    ListOrderSchema, FilterOrderParser
)
from apps.api_admin.logics import OrderResolver

router = APIRouter(route_class=Route, responses=ErrorSchema)


@router.get('', response_model=ListOrderSchema, status_code=200)
async def list_orders(
        parser: FilterOrderParser = Depends(FilterOrderParser)
):
    """the api of read list orders"""

    query = OrderResolver.list_orders(parser)
    total = await query.count()
    query = Pagination(query, parser.page, parser.pagesize or total).items()
    orders = await query.prefetch_related('owner')

    return ListOrderSchema(data={'total': total, 'orders': orders})
