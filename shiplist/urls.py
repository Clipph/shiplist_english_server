from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShipViewSet, home, ship_logs_view

router = DefaultRouter()
router.register(r'ships', ShipViewSet)

urlpatterns = [
    path('', home, name='home'),  # shows homepage at /
    path('ship_logs/', ship_logs_view,  name='ship_logs'),
    path('api/', include(router.urls)), # API at /api/ships/
]
