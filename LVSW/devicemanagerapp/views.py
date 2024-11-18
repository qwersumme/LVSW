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
