from django.shortcuts import render
from geopy.distance import geodesic
from django.shortcuts import get_object_or_404

from cargo.models import Cargo


def cargo_detail(request, cargo_id):
    cargo = get_object_or_404(Cargo, id=cargo_id)
    distance = calculate_distance(cargo.pick_up_location, cargo.delivery_location)
    return render(request, 'cargo_detail.html', {'cargo': cargo, 'distance': distance})


def calculate_distance(location1, location2):
    distance = geodesic((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).miles
    return distance
