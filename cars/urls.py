from django.urls import path
from cars.views import edit_car

urlpatterns = [
    path('car/<int:car_id>/edit', edit_car, name='edit_car'),
]