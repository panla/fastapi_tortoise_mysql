from tortoise import fields

from mixins import BaseModel, ModelMixin


class User(BaseModel, ModelMixin):
    cellphone = fields.CharField(max_length=16, null=False, description='手机号')
    name = fields.CharField(max_length=30, null=False, description='用户名')

    admin_user: fields.OneToOneRelation['AdminUser']
    questions: fields.ReverseRelation['Question']
    orders: fields.ReverseRelation['Order']

    class Meta:
        table = 'users'
        table_description = '用户表'
        unique_together = (('cellphone',),)

    @property
    async def is_admin_user(self) -> bool:
        """judge this user is admin_user or not"""

        obj = await AdminUser.get_or_none(user_id=self.id, is_delete=False)
        if obj:
            return True
        return False


class AdminUser(BaseModel, ModelMixin):
    user: fields.OneToOneRelation['User'] = fields.OneToOneField(
        model_name='models.User', related_name='admin_user', db_constraint=False, description='用户id')

    login_time = fields.DatetimeField(null=True, description='登录时间')
    token_expired = fields.DatetimeField(null=True, description='登录过期时间')

    class Meta:
        table = 'admin_users'
        table_description = '管理员表'


class Book(BaseModel, ModelMixin):
    name = fields.CharField(max_length=100, null=False, description='书名')
    price = fields.IntField(null=False, description='价格,分')
    sn = fields.CharField(max_length=100, null=False, description='序列号')

    class Meta:
        table = 'books'
        table_description = '书籍表'
        indexes = (('name',),)
        unique_together = (('sn',),)


class Car(BaseModel, ModelMixin):
    brand = fields.CharField(max_length=100, null=False, description='品牌')
    price = fields.IntField(null=False, description='价格,分')

    class Meta:
        table = 'cars'
        table_description = '汽车表'
        indexes = (('brand',),)


class Phone(BaseModel, ModelMixin):
    brand = fields.CharField(max_length=100, null=False, description='品牌')
    price = fields.IntField(null=False, description='价格,分')

    class Meta:
        table = 'phones'
        table_description = '手机表'
        indexes = (('brand',),)


class Question(BaseModel, ModelMixin):
    owner: fields.ForeignKeyRelation['User'] = fields.ForeignKeyField(
        model_name='models.User', related_name='questions', db_constraint=False)

    title = fields.CharField(max_length=100, null=False, description='问题')
    content = fields.TextField(description='问题内容')

    class Meta:
        table = 'questions'
        table_description = '问题表'


class Order(BaseModel, ModelMixin):
    owner: fields.ForeignKeyRelation['User'] = fields.ForeignKeyField(
        model_name='models.User', related_name='orders', db_constraint=False)

    amount = fields.BigIntField(null=False, description='订单总额')
    remarks = fields.CharField(max_length=300, description='订单备注')

    class Meta:
        table = 'orders'
        table_description = '订单表'
