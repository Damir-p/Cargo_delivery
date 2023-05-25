import random
import asyncio
from django.db import transaction

from cars.models import Car


def generate_random_location():
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    return latitude, longitude


async def update_car_locations():
    while True:
        await asyncio.sleep(180) 

        with transaction.atomic():
            cars = Car.objects.select_for_update().all()

            for car in cars:
                latitude, longitude = generate_random_location()
                car.location.latitude = latitude
                car.location.longitude = longitude
                car.location.save()


def start_update_task():
    asyncio.run(update_car_locations())


