__all__ = [
    'MaxMinValidator',
]

from typing import Union
from decimal import Decimal

from tortoise.validators import Validator, ValidationError


class MaxMinValidator(Validator):
    """
    A validator to validate the max value of given value whether greater than lte or not,
    the min value of given value whether less than gte or not

    max_value = 100, value == 100 ok, value == 101 error
    min_value = 1, value == 1 ok, value == 0 error
    """

    def __init__(
            self,
            max_value: Union[int, float, Decimal] = None,
            min_value: Union[int, float, Decimal] = None
    ):
        self.max_value = max_value
        self.min_value = min_value

    def __call__(self, value: Union[int, float], *args, **kwargs):
        if self.max_value is not None and value > self.max_value:
            raise ValidationError(f'{value} > {self.max_value}')

        if self.min_value is not None and value < self.min_value:
            raise ValidationError(f'{value} < {self.min_value}')
