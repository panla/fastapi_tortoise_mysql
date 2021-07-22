from apps.models import Question


def filter_questions(params: dict):
    """search/filter questions"""

    query = Question.filter(is_delete=False)
    return query
