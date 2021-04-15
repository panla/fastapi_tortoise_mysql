from tortoise import fields

from apps.mixins.model import BaseModel


class User(BaseModel):

    cellphone = fields.CharField(max_length=16, null=False, unique=True, description='手机号')
    name = fields.CharField(max_length=30, null=False, description='用户名')

    class Meta:
        table = 'users'
        table_description = '用户表'
