from tortoise.models import QuerySet

from extensions import Pagination
from apps.modules import ResourceOp
from apps.models import Car
from apps.api_admin.schemas import CreateCarParser, PatchCarParser, FilterCarParser


class CarResolver:

    @classmethod
    async def read_car(cls, car_id: int):

        _, instance = await ResourceOp(Car, car_id).instance(is_delete=False)
        return instance

    @classmethod
    async def list_cars(cls, parser: FilterCarParser) -> dict:
        """search/filter cars"""

        query = Car.filter(is_delete=False)
        if parser.brand:
            query = query.filter(brand__icontains=parser.brand)

        total = await query.count()
        result = await Pagination(query, parser.page, parser.page_size or total).items()

        return {'total': total, 'cars': result}

    @classmethod
    def create_car(cls, parser: CreateCarParser):
        """ create one car"""

        params = parser.dict()
        return Car.create(**params)

    @classmethod
    async def patch_car(cls, car_id: int, parser: PatchCarParser):
        """update one car"""

        instances, _ = await ResourceOp(Car, car_id).instance()

        params = parser.dict()
        patch_params = dict()

        for k, v in params.items():
            if v is not None:
                patch_params[k] = v
        if patch_params:
            await instances.update(**patch_params)

        return await instances.first()
