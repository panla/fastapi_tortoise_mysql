from fastapi import APIRouter, BackgroundTasks

from extensions import Route, error_schema, resp_success
from apps.api_admin.entities import CreateCodeSchema, CreateCodeParser
from apps.api_admin.logics import create_sms_code, send_sms_task

router = APIRouter(route_class=Route, responses=error_schema)


@router.post('', response_model=CreateCodeSchema, status_code=201)
async def create_code(parser: CreateCodeParser, background_tasks: BackgroundTasks):
    """the api of create sms code

    and background_task demo
    """

    code = await create_sms_code(parser)

    # background_tasks.add_task(send_sms_task, params=params, code=code)

    return resp_success(data={'success': True, 'code': code})
