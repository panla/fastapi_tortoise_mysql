from fastapi import APIRouter
from fastapi import Query

from apps.models import Question
from apps.entities.v1.admin.question import ReadQuestionSchema, ListQuestionSchema
from apps.utils.response import resp_200, resp_404, error_response
from apps.extension.route import Route

router = APIRouter(route_class=Route)


@router.get('/{q_id}', response_model=ReadQuestionSchema, status_code=200, responses=error_response)
async def read_question(q_id):
    """问题详情接口"""

    query = await Question.filter(id=q_id).first()
    if query:
        question = await Question.ModelCreator().from_tortoise_orm(query)
        return resp_200(data=question)
    resp_404(message='该问题不存在')


@router.get('', response_model=ListQuestionSchema, status_code=200, responses=error_response)
async def list_question(
        page: int = Query(default=1, description='页数', gte=1),
        pagesize: int = Query(default=10, description='每页数', gte=1, lte=40)
):
    """问题列表接口"""

    query = Question.all()
    total = await query.count()
    questions = query.offset(page - 1).limit(pagesize)

    questions = await Question.QuerySetCreator().from_queryset(questions)
    questions = questions.dict().get('__root__')
    return resp_200(data={'total': total, 'questions': questions})
