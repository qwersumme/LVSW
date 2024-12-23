# devicemanagerapp/urls.py
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.devicemanagerappindex),
    path('create_manufacturer/', views.create_manufacturer, name='create_manufacturer'),
    path('manufacturer/', views.manufacturer_list, name='hersteller_liste'),
    path('search-manufacturer/', views.search_manufacturer, name='search_manufacturer'),
    path('create-device/<int:hersteller_id>/', views.create_device, name='create_device'),
    path('search-manufacturer/', views.search_manufacturer, name='search_manufacturer'),
    path('device-list/', views.device_list, name='device_list'),
    path('delete-geraetetyp/<int:geraetetypid>/', views.delete_geraetetyp, name='delete_geraetetyp'),
    path('show-device/<int:geraete_id>/', views.show_device, name='show_device'),
    path('edit-device/<int:geraete_id>/', views.edit_device, name='edit_device'),
    path('generate-barcodes/<int:geraetetypid>/', views.generate_barcodes, name='generate_barcodes'),
    path('barcodes-list/', views.barcodes_list, name='barcodes_list'),
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
    path('group_list/', views.group_list, name="group_list"),
    path('group-details/<int:barcode_id>/', views.group_details, name='group_details'),
    path('test-gruppen/', views.test_gruppen_view, name='test_gruppen'),
]