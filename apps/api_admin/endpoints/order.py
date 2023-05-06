from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK

from extensions import Route, ErrorSchema
from apps.api_admin.schemas import (
    ListOrderSchema, FilterOrderParser
)
from apps.api_admin.logics import OrderResolver

router = APIRouter(route_class=Route, responses=ErrorSchema)


@router.get('', response_model=ListOrderSchema, status_code=HTTP_200_OK)
async def list_orders(
        parser: FilterOrderParser = Depends(FilterOrderParser)
):
    """the api of read list orders"""

    data = await OrderResolver.list_orders(parser)

    return ListOrderSchema(data=data)
