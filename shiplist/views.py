from rest_framework import viewsets
from .models import Ship, Rule
from .serializers import ShipSerializer
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.utils.timezone import now

class ShipViewSet(viewsets.ModelViewSet):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer

def ship_logs_view(request):
    ship_logs = Ship.objects.all().order_by('-ship_no')
    return render(request, 'shiplist/ship_logs.html', {'ships': ship_logs})

def pending_ships_view(request):
        pending_ships = Ship.objects.filter(status=0)
        return render(request, 'shiplist/pending_ships.html', {'ships': pending_ships})

def untracked_ships_view(request):
    untracked_ships = Ship.objects.filter(status=1)
    return render(request, 'shiplist/untracked_ships.html', {'ships': untracked_ships})

def sunken_ships_view(request):
    sunken_ships = Ship.objects.filter(status=3)
    return render(request, 'shiplist/sunken_ships.html', {'ships': sunken_ships})

def new_ships_view(request):
    seven_days_ago = timezone.now() - timedelta(days=7)
    new_ships = Ship.objects.filter(shipped_date__gte=seven_days_ago)
    return render(request, 'shiplist/new_ships.html', {'ships': new_ships})

def home(request):
    sailing_ships = Ship.objects.filter(status=2).order_by('-ship_no')
    current_time = now()  # Django timezone-aware server time
    return render(request, 'shiplist/index.html', {
        'ships': sailing_ships,
        'current_time': current_time,
    })

def about(request):
    return render(request, 'shiplist/about.html')

def rules(request):
    rules = Rule.objects.all().order_by('article_number')
    return render(request, 'shiplist/rules.html', {'rules': rules})