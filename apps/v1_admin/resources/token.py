from fastapi import APIRouter, Request

from apps.utils import resp_success
from apps.extensions import Route, error_response
from apps.modules import authentic
from apps.v1_admin.entities import CreateTokenParser, TokenSchema

router = APIRouter(route_class=Route, responses=error_response)


@router.post('', response_model=TokenSchema, status_code=201)
async def create_token(parser: CreateTokenParser):
    """the api of login and get token"""

    data = await authentic(parser.cellphone, parser.code)
    return resp_success(data=data)
