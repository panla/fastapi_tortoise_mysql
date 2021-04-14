from typing import Optional

from fastapi import APIRouter
from fastapi import Query

from apps.models import User, Question
from apps.entities.v1.admin.question import ReadQuestionSchema, ListQuestionSchema
from apps.utils.response import resp_200, resp_201, resp_404, error_response
from apps.extend.route import Route

router = APIRouter(route_class=Route)


@router.get('/{q_id}', response_model=ReadQuestionSchema, status_code=200, responses=error_response)
async def read_question(q_id):
    question = await Question.get_or_none(id=q_id)
    if question:
        await Question.get_owner(question)
        return resp_200(data=question)
    resp_404(message='该问题不存在')


@router.get('', response_model=ListQuestionSchema, status_code=200, responses=error_response)
async def list_question(
        page: int = Query(default=1, description='页数', gte=1),
        pagesize: int = Query(default=10, description='每页数', gte=1, lte=40)
):
    questions = Question.all()
    total = await questions.count()
    questions = await questions.offset(page - 1).limit(pagesize)
    await Question.get_owner(questions)

    return resp_200(data={'total': total, 'questions': questions})
