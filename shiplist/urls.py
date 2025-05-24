from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShipViewSet, home

router = DefaultRouter()
router.register(r'ships', ShipViewSet)

urlpatterns = [
    path('', home, name='home'),  # shows homepage at /
    path('api/', include(router.urls)), # API at /api/ships/
]
