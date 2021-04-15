from tortoise import fields

from apps.mixins.model import BaseModel


class Question(BaseModel):

    owner_id = fields.BigIntField(index=True, description='提问者')
    title = fields.CharField(max_length=100, null=False, description='问题')
    content = fields.TextField(description='问题内容')

    class Meta:
        table = 'questions'
        table_description = '问题表'

    @classmethod
    async def get_owner(cls, instance):
        from apps.models import User

        if isinstance(instance, list):
            for question in instance:
                question.owner = await User.get_or_none(id=question.id)
        else:
            instance.owner = await User.get_or_none(id=instance.id)
