from fastapi import APIRouter

from extensions import Route, error_response, resp_success
from apps.api_test.logics import RedisTestResolver

router = APIRouter(route_class=Route, responses=error_response)


@router.post('/redis')
async def redis_operator_test():
    await RedisTestResolver.test_set()

    return resp_success(data=True)
