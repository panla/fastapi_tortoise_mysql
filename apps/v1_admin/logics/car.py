from tortoise.models import QuerySet

from apps.models import Car


def filter_cars(params: dict) -> QuerySet:
    """search/filter cars"""

    cars = Car.filter(is_delete=False)
    if params.get('brand'):
        cars = cars.filter(brand__icontains=params['brand'])
    return cars
