# devicemanagerapp/urls.py
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.customermanagementapp),
    path('kunden-liste/', views.kunden_liste, name='kunden_liste'),
    path('kunde-erstellen/', views.kunde_erstellen, name='kunde_erstellen'),
]