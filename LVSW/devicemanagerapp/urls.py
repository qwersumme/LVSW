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
    path('delete-geraetetyp/<int:geraetetypid>/', views.delete_geraetetyp, name='delete_geraetetyp'),
    path('show-device/<int:geraete_id>/', views.show_device, name='show_device'),
    path('edit-device/<int:geraete_id>/', views.edit_device, name='edit_device'),
    path('generate-barcodes/<int:geraetetypid>/', views.generate_barcodes, name='generate_barcodes'),
    path('barcodes-liste/', views.barcodes_liste, name='barcodes_liste'),
    #path('ajax/search/barcodes/', views.barcode_ajax_search, name='ajax_search'), #for later
    path('barcode-details/<int:barcode_id>/', views.barcode_details, name='barcode_details'),
    path('delete-barcode/<int:barcode_id>/', views.delete_barcode, name='delete_barcode'),
    path('edit-barcode/<int:barcode_id>/', views.edit_barcode, name='edit_barcode'),
    path('select-status/', views.select_status, name='select_status'),
    path('update-status/', views.update_status, name='update_status'),
    path('barcode/<str:number>/', views.barcode_view, name='barcode'),
    path('selected-barcodes/', views.show_selected_barcodes, name='show_selected_barcodes'),
    path('erstelle-gruppe/', views.gruppe_erstellen, name="create_group1"),
    path('erstelle-gruppen-barcode/<str:name>/', views.generate_barcode_for_group, name="create_group2"),
    path('group_list/', views.group_list, name="group_list")
]