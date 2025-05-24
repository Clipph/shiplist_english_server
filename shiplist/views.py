from rest_framework import viewsets
from .models import Ship
from .serializers import ShipSerializer
from django.shortcuts import render

class ShipViewSet(viewsets.ModelViewSet):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer

def ship_list_view(request):
    ships = Ship.objects.all()
    return render(request, 'shiplist/index.html', {'ships': ships})