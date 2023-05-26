from rest_framework import serializers
from cargo.models import Cargo
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from location.models import Location

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'


def create_cargo(request):
    pick_up_zip = request.POST.get('pick_up_zip')
    delivery_zip = request.POST.get('delivery_zip')
    weight = request.POST.get('weight')
    description = request.POST.get('description')


    pick_up_location = get_object_or_404(Location, zipcode=pick_up_zip)
    delivery_location = get_object_or_404(Location, zipcode=delivery_zip)

    cargo = Cargo.objects.create(
        pick_up_location=pick_up_location,
        delivery_location=delivery_location,
        weight=weight,
        description=description
    )

    serializer = CargoSerializer(cargo)
    return JsonResponse(serializer.data)

from rest_framework import serializers
from .models import Cargo

class CargoSerializer(serializers.ModelSerializer):
    pick_up_location = serializers.CharField(source='pick_up_location.name')
    delivery_location = serializers.CharField(source='delivery_location.name')
    distance = serializers.SerializerMethodField()
    car_count = serializers.SerializerMethodField()

    def get_distance(self, obj):
        pickup_coords = (obj.pick_up_location.latitude, obj.pick_up_location.longitude)
        delivery_coords = (obj.delivery_location.latitude, obj.delivery_location.longitude)
        dist = distance.distance(pickup_coords, delivery_coords).km
        return dist

    def get_car_count(self, obj):
        cars_within_distance = Car.objects.filter(
            location__distance_lte=(obj.pick_up_location.location, obj.distance)
        )
        car_count = cars_within_distance.count()
        return car_count

    class Meta:
        model = Cargo
        fields = ['id', 'pick_up_location', 'delivery_location', 'distance', 'car_count']
