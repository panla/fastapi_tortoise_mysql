from tortoise import fields

from apps.mixins.model import BaseModel


class Order(BaseModel):

    owner = fields.ForeignKeyField('models.User', related_name='orders', db_constraint=False)
    amount = fields.BigIntField(null=False, description='订单总额')
    remarks = fields.CharField(max_length=300, description='订单备注')

    class Meta:
        table = 'orders'
        table_description = '订单表'
