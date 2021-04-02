from tortoise import fields
from tortoise.models import Model


class BaseModel(Model):

    id = fields.BigIntField(pk=True, description='主键')
    created_at = fields.DatetimeField(auto_now_add=True, null=False, description='创建时间')
    updated_at = fields.DatetimeField(auto_now=True, null=False, description='更新时间')
    is_delete = fields.BooleanField(null=False, default=False, description='删除标识')

    class Meta:
        abstract = True
