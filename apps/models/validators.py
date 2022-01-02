from typing import Union
from decimal import Decimal

from tortoise.validators import Validator, ValidationError


class MaxMinValidator(Validator):
    """
    A validator to validate the value of given whether greater than max_value or not,
    the value of given whether less than min_value or not

    max_value = 100, value == 100 ok, value == 101 error
    min_value = 1, value == 1 ok, value == 0 error

    MaxMinValidator(10, 5)
    """

    def __init__(
            self,
            min_value: Union[int, float, Decimal] = None,
            max_value: Union[int, float, Decimal] = None
    ):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value: Union[int, float], *args, **kwargs):
        if not isinstance(value, (int, float, Decimal)):
            raise ValidationError("Value must be a numeric value and is required")

        if self.min_value is not None and value < self.min_value:
            raise ValidationError(f"Value should be greater or equal to {self.min_value}")

        if self.max_value is not None and value > self.max_value:
            raise ValidationError(f"Value should be less or equal to {self.max_value}")
