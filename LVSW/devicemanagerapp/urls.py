# devicemanagerapp/urls.py
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.devicemanagerappindex),
    path('herstellererstellen/', views.hersteller_erstellen, name='hersteller_erstellen'),
    path('hersteller/', views.hersteller_liste, name='hersteller_liste'),path('suche-hersteller/', views.suche_hersteller, name='suche_hersteller'),
    path('erstelle-geraet/<int:hersteller_id>/', views.erstelle_geraet, name='erstelle_geraet'),
    path('suche-hersteller/', views.suche_hersteller, name='suche_hersteller'),
    path('geraete-liste/', views.geraete_liste, name='geraete_liste'),
    path('show-device/<int:geraete_id>/', views.show_device, name='show_device'),
    path('edit-device/<int:geraete_id>/', views.edit_device, name='edit_device'),
]