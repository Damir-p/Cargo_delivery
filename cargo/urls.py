from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cargo import views


router = DefaultRouter()
router.register(r'cargo', views.CargoViewSet)

urlpatterns = [
    path('cargo/<int:cargo_id>/edit', views.edit_cargo, name='edit_cargo'),
    path('cargo/router', include(router.urls)),
    path('cargo/create', views.create_cargo, name='create_cargo'),
    path('cargo/list', views.get_cargo_list, name='get_cargo_list'),
    path('cargo/<int:cargo_id>', views.get_cargo_info, name='get_cargo_info'),
    path('cargo/<int:cargo_id>/delete', views.delete_cargo, name='delete_cargo'),
]


