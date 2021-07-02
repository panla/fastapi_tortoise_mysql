from tortoise import fields

from apps.mixins.model import BaseModel


class Book(BaseModel):

    name = fields.CharField(max_length=100, null=False, description='书名')
    price = fields.IntField(null=False, description='价格,分')
    sn = fields.CharField(max_length=100, null=False, description='序列号')

    class Meta:
        table = 'books'
        table_description = '书籍表'
        indexes = (('name',),)
        unique_together = (('sn',),)
