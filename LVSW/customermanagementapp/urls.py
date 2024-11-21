# devicemanagerapp/urls.py
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.customermanagementapp),
    path('kunden-liste/', views.kunden_liste, name='kunden_liste'),
    path('kunde-erstellen/', views.kunde_erstellen, name='kunde_erstellen'),
    path('events/', views.event_list, name='event_list'),
    #path('events_edit/<int:pk>/', views.edit_event, name='edit_event'),
    #path('events/create/<int:kundenid>/', views.create_event, name='create_event'),
]