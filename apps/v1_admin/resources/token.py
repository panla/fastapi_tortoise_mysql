from fastapi import APIRouter
from fastapi import Request

from apps.extensions import Route, error_response
from apps.modules import authentic
from apps.v1_admin.entities import CreateTokenParser
from apps.v1_admin.entities import TokenSchema

router = APIRouter(route_class=Route)


@router.post('', response_model=TokenSchema, status_code=201, responses=error_response)
async def create_token(request: Request, parser: CreateTokenParser):
    data = await authentic(request, parser.cellphone, parser.code)
    return data
