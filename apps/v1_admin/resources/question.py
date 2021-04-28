from fastapi import APIRouter
from fastapi import Depends

from apps.models import Question, AdminUser
from apps.utils import raise_404, error_response
from apps.extension.route import Route
from apps.v1_admin.libs.token import get_current_admin_user
from apps.v1_admin.entities.question import ReadQuestionSchema, ListQuestionSchema
from apps.v1_admin.entities.question import read_exclude, list_exclude, read_computed, list_computed
from apps.v1_admin.entities.question import filter_params

router = APIRouter(route_class=Route)


@router.get('/{q_id}', response_model=ReadQuestionSchema, status_code=200, responses=error_response)
async def read_question(q_id: int, admin_user: AdminUser = Depends(get_current_admin_user)):
    """问题详情接口"""

    query = await Question.filter(id=q_id).first()
    if query:
        question = await Question.ModelCreator(exclude=read_exclude, computed=read_computed).from_tortoise_orm(query)
        return question
    raise_404(message='该问题不存在')


@router.get('', response_model=ListQuestionSchema, status_code=200, responses=error_response)
async def list_question(
        params: dict = Depends(filter_params),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """问题列表接口"""

    query = Question.all()
    total = await query.count()

    query = Question.paginate(query, params['page'], params.get('pagesize') or total)

    questions = await Question.QuerySetCreator(exclude=list_exclude, computed=list_computed).from_queryset(query)
    questions = questions.dict().get('__root__')
    return {'total': total, 'questions': questions}
