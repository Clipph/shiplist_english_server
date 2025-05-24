from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShipViewSet, home, ship_logs_view, about, rules

router = DefaultRouter()
router.register(r'ships', ShipViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('ship_logs/', ship_logs_view,  name='ship_logs'),
    path('rules/', rules, name='rules'),
    path('about/', about, name='about'),
    path('api/', include(router.urls)),
]
