from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', include('shiplist.urls')),
    path('admin/', admin.site.urls),
    # path('api/', include('shiplist.urls')),
]
