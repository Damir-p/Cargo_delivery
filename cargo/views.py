from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from geopy import distance
import json
from geopy.distance import geodesic

from cargo.models import Cargo
from cars.models import Car
from cargo.serializers import CargoSerializer
from location.models import Location



class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


def create_cargo(request):
    pick_up_zip = request.POST.get('pick_up_zip')
    delivery_zip = request.POST.get('delivery_zip')
    weight = request.POST.get('weight')
    description = request.POST.get('description')
    
    pick_up_location = get_object_or_404(
        Location, 
        zipcode=pick_up_zip
        )
    delivery_location = get_object_or_404(
        Location, 
        zipcode=delivery_zip)

    cargo = Cargo.objects.create(
        pick_up_location=pick_up_location, 
        delivery_location=delivery_location, 
        weight=weight, 
        description=description
        )
    return JsonResponse({'cargo_id': cargo.id})

def get_cargo_list(request):
    cargos = Cargo.objects.all()
    cargo_list = []
    
    for cargo in cargos:
        pickup = cargo.pick_up_location
        delivery = cargo.delivery_location
        
        pickup_coords = (pickup.latitude, pickup.longitude)
        delivery_coords = (delivery.latitude, delivery.longitude)
        dist = distance.distance(pickup_coords, delivery_coords).km
        print(f"Расстояние между pick-up и delivery: {dist} км")
        
        cars_within_distance = Car.objects.filter(
            location__distance_lte=(pickup.Location, dist) 
            )

        car_count = cars_within_distance.count()
        
        cargo_info = {
            'id': cargo.id,
            'pick_up_location': pickup.name,
            'delivery_location': delivery.name,
            'distance': distance,
            'car_count': car_count
        }
        
        cargo_list.append(cargo_info)    
    return JsonResponse({'cargo_list': json.dumps(cargo_list)})

def get_cargo_info(request, cargo_id):
    cargo = get_object_or_404(Cargo, id=cargo_id)
    pickup = cargo.pick_up_location
    delivery = cargo.delivery_location

    pickup_coords = (pickup.latitude, pickup.longitude)
    delivery_coords = (delivery.latitude, delivery.longitude)
    distance = geodesic(pickup_coords, delivery_coords).km

    cars = Car.objects.all()
    car_info_list = []

    for car in cars:
        car_coords = (car.current_location.latitude, car.current_location.longitude)
        car_distance = geodesic(pickup_coords, car_coords).km
        car_info = {
            'car_number': car.unique_number,
            'distance': car_distance
        }
        car_info_list.append(car_info)

    cargo_info = {
        'id': cargo.id,
        'pick_up_location': pickup.city,
        'delivery_location': delivery.city,
        'weight': cargo.weight,
        'description': cargo.description,
        'cars': car_info_list
    }
    return JsonResponse({'cargo_info': cargo_info})
    
    
def edit_cargo(request, cargo_id):
    cargo = get_object_or_404(Cargo, id=cargo_id)
    weight = request.POST.get('weight')
    description = request.POST.get('description')
    
    if weight is not None:
        cargo.weight = weight
    
    if description is not None:
        cargo.description = description
    cargo.save()
    return JsonResponse({'message': 'Cargo updated successfully'})



def delete_cargo(request, cargo_id):
    cargo = get_object_or_404(Cargo, id=cargo_id)
    cargo.delete()    
    return JsonResponse({'message': 'Cargo deleted successfully'})


def get_filtered_cargos(request):
    min_weight = request.GET.get('min_weight')
    max_weight = request.GET.get('max_weight')
    max_distance = request.GET.get('max_distance')
    
    cargos = Cargo.objects.all()
    
    if min_weight is not None:
        cargos = cargos.filter(weight__gte=min_weight)
    if max_weight is not None:
        cargos = cargos.filter(weight__lte=max_weight)
    filtered_cargos = []
    for cargo in cargos:        
        return JsonResponse({'cargos': filtered_cargos})
