from fastapi import APIRouter
from fastapi import Request

from apps.utils import error_response
from apps.extension.route import Route
from apps.libs.admin.token import authentic
from apps.entities.v1.admin.token import CreateTokenParameter
from apps.entities.v1.admin.token import TokenSchema

router = APIRouter(route_class=Route)


@router.post('', response_model=TokenSchema, status_code=201, responses=error_response)
async def create_token(request: Request, params: CreateTokenParameter):
    data = await authentic(request, params.cellphone, params.code)
    return data
