from tortoise import fields

from apps.mixins.model import BaseModel


class User(BaseModel):

    cellphone = fields.CharField(max_length=16, null=False, unique=True, description='手机号')
    name = fields.CharField(max_length=30, null=False, description='用户名')

    class Meta:
        table = 'users'
        table_description = '用户表'


class AdminUser(BaseModel):

    user_id = fields.BigIntField(null=False, unique=True, description='用户id')
    login_time = fields.DatetimeField(null=True, description='登录时间')
    token_expired = fields.DatetimeField(null=True, description='登录过期时间')

    class Meta:
        table = 'admin_users'
        table_description = '管理员表'
