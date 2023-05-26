from rest_framework import serializers
from cargo.models import Cargo
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from location.models import Location

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'
