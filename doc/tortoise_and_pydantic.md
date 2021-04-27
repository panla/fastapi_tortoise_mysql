# tortoise 和 pydantic

目前他们在异步方面的支持还不是特别完善

## 加载同步属性或同步方法

```python
from tortoise import fields
from tortoise import Model
from tortoise.contrib.pydantic import pydantic_model_creator

class Order(Model):

    amount = fields.BigIntField(null=False, description='订单总额')

    def discount(self):
        if self.amount > 10000:
            return 0.9
        if self.amount > 50000:
            return 0.8
        if self.amount > 100000:
            return 0.7
        return 1


Creator = pydantic_model_creator(Order, computed=('discount',))

Creator.from_tortoise_orm(await Order.get_or_none(id=1))

# 此时包含 discount 

```

## 加载关联关系

```python
from tortoise import fields
from tortoise import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Order(Model):

    owner = fields.ForeignKeyField('models.User', related_name='orders', db_constraint=False)

# db_constraint 决定是否实际生成外键约束
Creator = pydantic_model_creator(Order, computed=('owner',))

Creator.from_tortoise_orm(await Order.get_or_none(id=1))

# 此时包含 owner

```
