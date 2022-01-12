from fastapi import APIRouter

from extensions import Route, ErrorSchema
from apps.api_admin.entities import CreateTokenParser, TokenSchema
from apps.api_admin.logics import LoginResolver

router = APIRouter(route_class=Route, responses=ErrorSchema)


@router.post('', response_model=TokenSchema, status_code=201)
async def create_token(parser: CreateTokenParser):
    """the api of login and get token"""

    data = await LoginResolver.authentic(parser.cellphone, parser.code, 'AdminUser')
    return TokenSchema(data=data)
