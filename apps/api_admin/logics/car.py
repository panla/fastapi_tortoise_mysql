from tortoise.models import QuerySet

from apps.modules import ResourceOp
from apps.models import Car
from apps.api_admin.entities import CreateCarParser, PatchCarParser


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
    def create_car(cls, parser: CreateCarParser):
        """ create one car"""
        params = parser.dict()
        return Car.create(**params)

    @classmethod
    async def patch_car(cls, car_id: int, parser: PatchCarParser) -> Car:
        """update one car"""

        car: Car = await ResourceOp(Car, car_id).instance()

        params = parser.dict()
        patch_params = {}

        for k, v in params.items():
            if v is not None:
                patch_params[k] = v
        if patch_params:
            car = await car.update_from_dict(patch_params)
            await car.save()

        del patch_params

        return car
