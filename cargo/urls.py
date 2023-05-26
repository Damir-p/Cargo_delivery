# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from cargo import views


# router = DefaultRouter()
# router.register(r'cargo', views.CargoViewSet)


# urlpatterns = [
#     path('cargo/<int:cargo_id>/edit', views.edit_cargo, name='edit_cargo'),
#     path('cargo/router/', include(router.urls)),
#     path('cargo/create', views.create_cargo, name='create_cargo'),
#     path('cargo/list', views.get_cargo_list, name='get_cargo_list'),
#     path('cargo/<int:cargo_id>', views.get_cargo_info, name='get_cargo_info'),
#     path('cargo/<int:cargo_id>/delete', views.delete_cargo, name='delete_cargo'),
# ]

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

# Создаем экземпляр маршрутизатора
router = DefaultRouter()
router.register('cargos', CargoViewSet)

urlpatterns = [
    # URL-пути для API
    path('api/cargos/create/', create_cargo, name='create_cargo'),
    path('api/cargos/list/', get_cargo_list, name='get_cargo_list'),
    path('api/cargos/<int:cargo_id>/', get_cargo_info, name='get_cargo_info'),
    path('api/cargos/<int:cargo_id>/edit/', edit_cargo, name='edit_cargo'),
    path('api/cargos/<int:cargo_id>/delete/', delete_cargo, name='delete_cargo'),
    path('api/cargos/filter/', get_filtered_cargos, name='get_filtered_cargos'),
]

# Добавляем URL-пути маршрутизатора к основным URL-путям
urlpatterns += router.urls

