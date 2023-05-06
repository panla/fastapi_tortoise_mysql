from extensions import Pagination, NotFound
from apps.models import Question
from apps.api_admin.schemas import FilterQuestionParser


class QuestionResolver:

    @classmethod
    async def list_questions(cls, parser: FilterQuestionParser) -> dict:
        """search/filter questions"""

        query = Question.filter(is_delete=False)

        total = await query.count()
        query = Pagination(query, parser.page, parser.page_size or total).items()
        result = await query.prefetch_related('owner')

        return {'total': total, 'questions': result}

    @classmethod
    async def read_question(cls, question_id: int):
        query = await Question.filter(id=question_id).prefetch_related('owner').first()

        if query:
            return query
        raise NotFound(message=f'Question id = {question_id} 不存在')
