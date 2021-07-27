from fastapi import APIRouter, Depends, Path

from apps.extensions import Route, NotFound, error_response
from apps.utils import resp_success
from apps.models import Question, AdminUser
from apps.modules import get_current_admin_user
from apps.v1_admin.entities import (
    ReadQuestionSchema, ListQuestionSchema, FilterCarParser
)
from apps.v1_admin.logics import filter_questions

router = APIRouter(route_class=Route)


@router.get('/{q_id}', response_model=ReadQuestionSchema, status_code=200, responses=error_response)
async def read_question(
        q_id: int = Path(..., description='问题id', ge=1),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """the api of read one question"""

    query = await Question.filter(id=q_id).prefetch_related('owner').first()
    if query:
        return resp_success(data=query)
    raise NotFound(message=f'Question {q_id} 不存在')


@router.get('', response_model=ListQuestionSchema, status_code=200, responses=error_response)
async def list_question(
        parser : FilterCarParser = Depends(FilterCarParser),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """the api of read list questions"""

    params = parser.dict()
    query = filter_questions(params)
    query = query.prefetch_related('owner')
    total = await query.count()

    query = await Question.paginate(query, params['page'], params.get('pagesize') or total)

    return resp_success(data={'total': total, 'questions': query})
