from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import HerstellerForm, GeraetetypForm
from .models import Hersteller_view, Geraetetyp, Hersteller

# Create your views here.


def devicemanagerappindex(request):
    return render(request, 'devicemanagerapp/devicemanagerappindex.html')

def hersteller_erstellen(request):
    if request.method == 'POST':
        form = HerstellerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hersteller wurde erfolgreich erstellt!')
            return redirect('hersteller_erstellen')
    else:
        form = HerstellerForm()
    return render(request, 'devicemanagerapp/hersteller_erstellen.html', {'form': form})

def hersteller_liste(request):
    hersteller = Hersteller_view.objects.all()  # Alle Hersteller aus der Datenbank abrufen
    return render(request, 'devicemanagerapp/hersteller_liste.html', {'hersteller': hersteller})

def suche_hersteller(request):
    query = request.GET.get('q', '')  # Suchfeld
    hersteller = Hersteller.objects.filter(name__icontains=query).order_by('name')
    return render(request, 'devicemanagerapp/suche_hersteller.html', {'hersteller': hersteller, 'query': query})

def erstelle_geraet(request, hersteller_id):
    # Hersteller aus der ID in der URL abrufen
    hersteller = get_object_or_404(Hersteller, herstellerid=hersteller_id)

    if request.method == 'POST':
        form = GeraetetypForm(request.POST)
        if form.is_valid():
            geraet = form.save(commit=False)
            # Hersteller für das Gerät setzen
            geraet.hersteller = hersteller
            geraet.save()
            return redirect('suche_hersteller')  # Nach dem Speichern zurück zur Suchseite
    else:
        # Initialisiere das Formular ohne Daten
        form = GeraetetypForm(initial={'herstellerid':hersteller_id})

    return render(request, 'devicemanagerapp/erstelle_geraet.html', {'form': form, 'hersteller': hersteller})

def geraete_liste(request):
    # Suchfunktion
    query = request.GET.get('q', '')  # Suchparameter aus der URL abrufen
    if query:
        geraete = Geraetetyp.objects.filter(modellbezeichnung__icontains=query).select_related('herstellerid')  # Suche in der Modellbezeichnung
    else:
        geraete = Geraetetyp.objects.all().select_related('herstellerid')  # Alle Geräte abrufen
    
    return render(request, 'devicemanagerapp/geraete_liste.html', {'geraete': geraete, 'query': query})

def show_device(request, geraete_id):
    # Gerät basierend auf der Geräte-ID abrufen
    geraetetyp = get_object_or_404(Geraetetyp, geraetetypid=geraete_id)
    return render(request, 'devicemanagerapp/show_devices.html', {'geraetetyp': geraetetyp})

def edit_device(request, geraete_id):
    # Gerät basierend auf der Geräte-ID abrufen
    geraetetyp = get_object_or_404(Geraetetyp, geraetetypid=geraete_id)

    if request.method == 'POST':
        # Formular mit den POST-Daten binden
        form = GeraetetypForm(request.POST, instance=geraetetyp)
        if form.is_valid():
            form.save()
            return redirect('show_device', geraete_id=geraete_id)  # Weiterleitung zur Detailseite
    else:
        # Formular mit den aktuellen Werten initialisieren
        form = GeraetetypForm(instance=geraetetyp)

    return render(request, 'devicemanagerapp/edit_device.html', {'form': form, 'geraetetyp': geraetetyp})
