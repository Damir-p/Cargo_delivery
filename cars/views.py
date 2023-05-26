from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from cars.models import Car
from location.models import Location
from cars.tasks import start_update_task
from cars.serializers import CarSerializer

def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    location_zip = request.POST.get('location_zip')
    location = get_object_or_404(Location, zipcode=location_zip)
    car.location = location
    car.save()    
    return JsonResponse({'message': 'Car updated successfully'})


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

# start_update_task() # обновление машин