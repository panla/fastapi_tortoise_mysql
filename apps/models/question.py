from tortoise import fields

from apps.mixins.model import BaseModel, ModelMixin


class Question(BaseModel, ModelMixin):
    owner = fields.ForeignKeyField('models.User', related_name='questions', db_constraint=False)
    title = fields.CharField(max_length=100, null=False, description='问题')
    content = fields.TextField(description='问题内容')

    class Meta:
        table = 'questions'
        table_description = '问题表'
        indexes = (('owner_id',),)
