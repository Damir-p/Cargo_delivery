from django.urls import path
from .views import (
    CargoViewSet,
    create_cargo,
    get_cargo_list,
    get_cargo_info,
    edit_cargo,
    delete_cargo,
    get_filtered_cargos
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cargos', CargoViewSet)

urlpatterns = [
    path('api/cargos/create/', create_cargo, name='create_cargo'),
    path('api/cargos/list/', get_cargo_list, name='get_cargo_list'),
    path('api/cargos/<int:cargo_id>/', get_cargo_info, name='get_cargo_info'),
    path('api/cargos/<int:cargo_id>/edit/', edit_cargo, name='edit_cargo'),
    path('api/cargos/<int:cargo_id>/delete/', delete_cargo, name='delete_cargo'),
    path('api/cargos/filter/', get_filtered_cargos, name='get_filtered_cargos'),
]

urlpatterns += router.urls

