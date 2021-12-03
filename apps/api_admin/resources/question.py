from fastapi import APIRouter, Depends, Path

from extensions import error_schema, resp_success, Route, Pagination
from apps.api_admin.entities import (
    ReadQuestionSchema, ListQuestionSchema, FilterCarParser
)
from apps.api_admin.logics import QuestionResolver

router = APIRouter(route_class=Route, responses=error_schema)


@router.get('/{q_id}', response_model=ReadQuestionSchema, status_code=200)
async def read_question(
        q_id: int = Path(..., description='问题id', ge=1)
):
    """the api of read one question"""

    query = await QuestionResolver.read_question(q_id)
    return resp_success(data=query)


@router.get('', response_model=ListQuestionSchema, status_code=200)
async def list_question(
        parser: FilterCarParser = Depends(FilterCarParser)
):
    """the api of read list questions"""

    payload = parser.dict()

    query = QuestionResolver.list_questions(payload)
    total = await query.count()
    query = Pagination(query, payload['page'], payload['pagesize'] or total).items()
    result = await query.prefetch_related('owner')

    return resp_success(data={'total': total, 'questions': result})
