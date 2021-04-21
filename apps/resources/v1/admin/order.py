from fastapi import APIRouter

from apps.extension.route import Route
from apps.models import Order
from apps.entities.v1.admin.order import ListOrderSchema
from apps.utils.response import resp_200, error_response
from tortoise.contrib.pydantic import pydantic_queryset_creator

router = APIRouter(route_class=Route)


@router.get('', response_model=ListOrderSchema, status_code=200, responses=error_response)
async def list_orders():

    OrderPydanticQuerysetCreator = pydantic_queryset_creator(Order)
    query = Order.all()
    orders = OrderPydanticQuerysetCreator.from_queryset(query)

    total = await query.count()
    orders = await orders
    orders = orders.dict().get('__root__')
    return resp_200(data={'total': total, 'orders': orders})
