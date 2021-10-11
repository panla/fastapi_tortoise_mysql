from tortoise.models import QuerySet

from extensions import logger
from apps.modules import ResourceOp
from apps.models import Car


class CarResolver:

    @classmethod
    def read_car(cls, car_id: int):
        return ResourceOp(Car, car_id).instance(is_delete=False)

    @classmethod
    def list_cars(cls, params: dict) -> QuerySet:
        """search/filter cars"""

        query = Car.filter(is_delete=False)
        if params.get('brand'):
            query = query.filter(brand__icontains=params['brand'])
        return query

    @classmethod
    def create_car(cls, params: dict):
        """ create one car"""
        return Car.create(**params)

    @classmethod
    async def patch_car(cls, car_id: int, params: dict) -> Car:
        """update one car"""

        car: Car = await ResourceOp(Car, car_id).instance()
        patch_params = {}
        logger.info(params)
        for k, v in params.items():
            if v is not None:
                patch_params[k] = v
        if patch_params:
            car = await car.update_from_dict(patch_params)
            await car.save()
            logger.info(car.price)
        return car
