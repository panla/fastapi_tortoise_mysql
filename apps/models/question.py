from tortoise import fields

from apps.mixins.model import BaseModel


class Question(BaseModel):

    owner_id = fields.BigIntField(index=True, description='提问者')
    title = fields.CharField(max_length=100, null=False, description='问题')
    content = fields.TextField(description='问题内容')

    class Meta:
        table = 'questions'
