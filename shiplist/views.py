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

def pending_ships_view(request):
        pending_ships = Ship.objects.filter(status=0)
        return render(request, 'shiplist/pending_ships.html', {'ships': pending_ships})

def untracked_ships_view(request):
    untracked_ships = Ship.objects.filter(status=1)
    return render(request, 'shiplist/untracked_ships.html', {'ships': untracked_ships})

def sunken_ships_view(request):
    sunken_ships = Ship.objects.filter(status=3)
    return render(request, 'shiplist/sunken_ships.html', {'ships': sunken_ships})

def home(request): # show only sailing ships
    sailing_ships = Ship.objects.filter(status=2) 
    return render(request, 'shiplist/index.html', {'ships': sailing_ships})