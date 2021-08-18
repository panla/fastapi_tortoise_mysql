from fastapi import APIRouter, Path

from extensions import Route, error_response, resp_success, NotFound
from apps.models import Car
from apps.v1_admin.entities import ReadCarSchema

router = APIRouter(route_class=Route, responses=error_response)


@router.get('/speed/common', status_code=200)
async def test_speed_common():
    """the api of test wrk speed"""

    return resp_success(data={'success': True})


@router.get('/speed/cars/{c_id}', response_model=ReadCarSchema, status_code=200)
async def read_car(
        c_id: int = Path(..., description='汽车id', ge=1)
):
    """the api of read one car"""

    car = await Car.get_or_none(id=c_id, is_delete=False)
    if car:
        return resp_success(data=car)
    raise NotFound(message=f'Car {c_id} not exists')
