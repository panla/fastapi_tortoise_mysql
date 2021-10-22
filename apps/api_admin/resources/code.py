from fastapi import APIRouter, BackgroundTasks

from extensions import Route, error_response, resp_success
from apps.api_admin.entities import CreateCodeSchema, CreateCodeParser
from apps.api_admin.logics import create_sms_code, create_sms_code_task

router = APIRouter(route_class=Route, responses=error_response)


@router.post('', response_model=CreateCodeSchema, status_code=201, responses=error_response)
async def create_code(parser: CreateCodeParser, background_tasks: BackgroundTasks):
    """the api of create sms code

    and backgroundtask demo
    """

    params = parser.dict()

    code = await create_sms_code(params)

    background_tasks.add_task(create_sms_code_task, params=params, code=code)

    return resp_success(data={'success': True, 'code': code})
