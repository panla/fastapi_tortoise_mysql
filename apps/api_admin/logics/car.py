from tortoise.models import QuerySet

from extensions import NotFound
from apps.modules import ResourceOp
from apps.models import Car
from apps.api_admin.entities import CreateCarParser, PatchCarParser, FilterCarParser


class CarResolver:

    @classmethod
    def read_car(cls, car_id: int):

        return ResourceOp(Car, car_id).instance(is_delete=False)

    @classmethod
    def list_cars(cls, parser: FilterCarParser) -> QuerySet[Car]:
        """search/filter cars"""

        query = Car.filter(is_delete=False)
        if parser.brand:
            query = query.filter(brand__icontains=parser.brand)
        return query

    @classmethod
    def create_car(cls, parser: CreateCarParser):
        """ create one car"""

        params = parser.dict()
        return Car.create(**params)

    @classmethod
    async def patch_car(cls, car_id: int, parser: PatchCarParser):
        """update one car"""

        cars = Car.filter(id=car_id)
        car = await cars.first()
        if not car:
            raise NotFound(f'Model = Car, pk = {car_id} is not exists')

        params = parser.dict()
        patch_params = dict()

        for k, v in params.items():
            if v is not None:
                patch_params[k] = v
        if patch_params:
            await cars.update(**patch_params)

        return car
