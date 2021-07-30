from fastapi import APIRouter

from apps.extensions import Route, error_response
from apps.utils import resp_success

router = APIRouter(route_class=Route)


@router.get('', status_code=200, responses=error_response)
async def test_speed_common():
    """the api of test wrk speed"""

    return resp_success(data={'success': True})
