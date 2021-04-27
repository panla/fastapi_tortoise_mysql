from tortoise.models import QuerySet

from apps.models import Car


def filter_cars(params: dict) -> QuerySet:
    """搜索汽车"""

    cars = Car.all()
    if params.get('brand'):
        cars = cars.filter(brand__icontains=params['brand'])
    return cars
