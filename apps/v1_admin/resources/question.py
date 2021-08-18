from fastapi import APIRouter, Depends, Path

from extensions import Route, error_response, resp_success, NotFound, Pagination
from apps.models import Question, AdminUser
from apps.modules import get_current_admin_user
from apps.v1_admin.entities import (
    ReadQuestionSchema, ListQuestionSchema, FilterCarParser
)
from apps.v1_admin.logics import filter_questions

router = APIRouter(route_class=Route, responses=error_response)


@router.get('/{q_id}', response_model=ReadQuestionSchema, status_code=200)
async def read_question(
        q_id: int = Path(..., description='问题id', ge=1),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """the api of read one question"""

    query = await Question.filter(id=q_id).prefetch_related('owner').first()
    if query:
        return resp_success(data=query)
    raise NotFound(message=f'Question {q_id} 不存在')


@router.get('', response_model=ListQuestionSchema, status_code=200)
async def list_question(
        parser: FilterCarParser = Depends(FilterCarParser),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """the api of read list questions"""

    params = parser.dict()
    query = filter_questions(params)
    total = await query.count()
    query = Pagination(query, params['page'], params['pagesize'] or total).result()
    result = await query.prefetch_related('owner')

    return resp_success(data={'total': total, 'questions': result})
