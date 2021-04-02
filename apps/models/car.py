from tortoise import fields

from apps.mixins.model import BaseModel


class Car(BaseModel):

    brand = fields.CharField(max_length=100, null=False, index=True, description='品牌')
    price = fields.IntField(null=False, description='价格,分')

    class Meta:
        table = 'cars'
