from fastapi import APIRouter
from fastapi import Request

from apps.extensions import Route, error_response
from apps.modules import authentic
from apps.v1_admin.entities import CreateTokenParameter
from apps.v1_admin.entities import TokenSchema

router = APIRouter(route_class=Route)


@router.post('', response_model=TokenSchema, status_code=201, responses=error_response)
async def create_token(request: Request, params: CreateTokenParameter):
    data = await authentic(request, params.cellphone, params.code)
    return data
