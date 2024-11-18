# devicemanagerapp/urls.py
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.devicemanagerappindex),
    path('herstellererstellen/', views.hersteller_erstellen, name='hersteller_erstellen'),
    path('hersteller/', views.hersteller_liste, name='hersteller_liste'),
]