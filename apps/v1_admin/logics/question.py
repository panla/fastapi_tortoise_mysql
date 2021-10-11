from tortoise.models import QuerySet

from extensions import NotFound
from apps.models import Question


class QuestionResolver:

    @classmethod
    def list_questions(cls, params: dict) -> QuerySet:
        """search/filter questions"""

        query = Question.filter(is_delete=False)
        return query

    @classmethod
    async def read_question(cls, question_id: int):
        query = await Question.filter(id=question_id).prefetch_related('owner').first()

        if query:
            return query
        raise NotFound(message=f'Question id = {question_id} 不存在')
