from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShipViewSet, ship_list_view

router = DefaultRouter()
router.register(r'ships', ShipViewSet)

urlpatterns = [
    path('', ship_list_view, name='ship-list'),  # shows homepage at /
    path('api/', include(router.urls)),          # API at /api/ships/
]
