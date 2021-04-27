from tortoise import fields

from apps.mixins.model import BaseModel, ModelMixin


class User(BaseModel, ModelMixin):

    cellphone = fields.CharField(max_length=16, null=False, unique=True, description='手机号')
    name = fields.CharField(max_length=30, null=False, description='用户名')

    class Meta:
        table = 'users'
        table_description = '用户表'

    async def get_is_admin_user(self):
        """判断是否是管理员"""

        obj = await AdminUser.get_or_none(user_id=self.id, is_delete=False)
        if obj:
            return True
        return False


class AdminUser(BaseModel, ModelMixin):

    user = fields.OneToOneField(
        'models.User', related_name='admin_user', db_constraint=False, null=False, description='用户id')
    login_time = fields.DatetimeField(null=True, description='登录时间')
    token_expired = fields.DatetimeField(null=True, description='登录过期时间')

    class Meta:
        table = 'admin_users'
        table_description = '管理员表'
        unique_together = ('user_id',)
