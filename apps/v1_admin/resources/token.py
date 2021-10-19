from fastapi import APIRouter

from extensions import Route, error_response, resp_success
from apps.modules import TokenResolver
from apps.v1_admin.entities import CreateTokenParser, TokenSchema

router = APIRouter(route_class=Route, responses=error_response)


@router.post('', response_model=TokenSchema, status_code=201)
async def create_token(parser: CreateTokenParser):
    """the api of login and get token"""

    data = await TokenResolver.authentic(parser.cellphone, parser.code, 'AdminUser')
    return resp_success(data=data)
