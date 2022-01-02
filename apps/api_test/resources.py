from fastapi import APIRouter

from extensions import Route, resp_success
from conf.define import error_schema
from apps.api_test.logics import RedisTestResolver

router = APIRouter(route_class=Route, responses=error_schema)


@router.post('/redis')
async def redis_operator_test():
    await RedisTestResolver.test_set()

    return resp_success(data=True)
