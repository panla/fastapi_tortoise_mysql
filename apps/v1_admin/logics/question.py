from apps.models import Question


def filter_questions(params: dict):
    """搜索问题"""

    query = Question.filter(is_delete=False)
    return query


async def response_question(question: Question):
    """组合问题详情返回数据"""

    _question = question.to_json(selects=['id', 'title', 'content', 'created_time', 'updated_time'])
    _question['owner'] = await question.owner
    return _question


async def response_questions(questions):
    """组合问题列表返回数据"""

    _questions = []
    for question in questions:
        _question = question.to_json(selects=['id', 'title', 'content', 'created_time'])
        _question['owner'] = await question.owner
        _questions.append(_question)
    return _questions
