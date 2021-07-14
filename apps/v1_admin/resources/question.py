from fastapi import APIRouter
from fastapi import Depends
from fastapi import Path

from apps.extensions import Route, NotFound
from apps.utils import resp_success, error_response
from apps.models import Question, AdminUser
from apps.modules import get_current_admin_user
from apps.v1_admin.entities import ReadQuestionSchema, ListQuestionSchema
from apps.v1_admin.entities import filter_question_dependency
from apps.v1_admin.logics import filter_questions

router = APIRouter(route_class=Route)


@router.get('/{q_id}', response_model=ReadQuestionSchema, status_code=200, responses=error_response)
async def read_question(
        q_id: int = Path(..., description='问题id', ge=1),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """问题详情接口"""

    query = await Question.filter(id=q_id).prefetch_related('owner').first()
    if query:
        return resp_success(data=query)
    raise NotFound(message=f'Question {q_id} 不存在')


@router.get('', response_model=ListQuestionSchema, status_code=200, responses=error_response)
async def list_question(
        params: dict = Depends(filter_question_dependency),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """问题列表接口"""

    query = filter_questions(params)
    query = query.prefetch_related('owner')
    total = await query.count()

    query = await Question.paginate(query, params['page'], params.get('pagesize') or total)

    return resp_success(data={'total': total, 'questions': query})
