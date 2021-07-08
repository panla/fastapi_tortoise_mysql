from apps.models import Question


def filter_questions(params: dict):
    """搜索问题"""

    query = Question.filter(is_delete=False)
    return query
