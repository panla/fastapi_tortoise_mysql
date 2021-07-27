from tortoise.models import QuerySet

from apps.models import Question


def filter_questions(params: dict) -> QuerySet:
    """search/filter questions"""

    query = Question.filter(is_delete=False)
    return query
