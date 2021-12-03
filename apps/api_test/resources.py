from fastapi import APIRouter

from extensions import error_schema, resp_success, Route
from apps.api_test.logics import RedisTestResolver

router = APIRouter(route_class=Route, responses=error_schema)


@router.post('/redis')
async def redis_operator_test():
    await RedisTestResolver.test_set()

    return resp_success(data=True)
