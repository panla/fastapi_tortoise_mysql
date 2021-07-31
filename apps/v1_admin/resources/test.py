from fastapi import APIRouter, Path

from apps.extensions import Route, NotFound, error_response
from apps.utils import resp_success
from apps.models import Car
from apps.v1_admin.entities import ReadCarSchema

router = APIRouter(route_class=Route)


@router.get('/speed/common', status_code=200, responses=error_response)
async def test_speed_common():
    """the api of test wrk speed"""

    return resp_success(data={'success': True})


@router.get('/speed/cars/{c_id}', response_model=ReadCarSchema, status_code=200, responses=error_response)
async def read_car(
        c_id: int = Path(..., description='汽车id', ge=1)
):
    """the api of read one car"""

    car = await Car.get_or_none(id=c_id, is_delete=False)
    if car:
        return resp_success(data=car)
    raise NotFound(message=f'Car {c_id} not exists')
