from fastapi import APIRouter, Depends, Path

from extensions import Route, Pagination, ErrorSchema
from apps.api_admin.schemas import (
    ReadQuestionSchema, ListQuestionSchema, FilterQuestionParser
)
from apps.api_admin.logics import QuestionResolver

router = APIRouter(route_class=Route, responses=ErrorSchema)


@router.get('/{q_id}', response_model=ReadQuestionSchema, status_code=200)
async def read_question(
        q_id: int = Path(..., description='问题id', ge=1)
):
    """the api of read one question"""

    query = await QuestionResolver.read_question(q_id)
    return ReadQuestionSchema(data=query)


@router.get('', response_model=ListQuestionSchema, status_code=200)
async def list_question(
        parser: FilterQuestionParser = Depends(FilterQuestionParser)
):
    """the api of read list questions"""

    query = QuestionResolver.list_questions(parser)
    total = await query.count()
    query = Pagination(query, parser.page, parser.pagesize or total).items()
    result = await query.prefetch_related('owner')

    return ListQuestionSchema(data={'total': total, 'questions': result})
