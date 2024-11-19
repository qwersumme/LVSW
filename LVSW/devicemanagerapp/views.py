from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .forms import HerstellerForm, GeraetetypForm, BarcodeelementForm, ZustandSelectionForm, BarcodeSingleInputForm
from .models import Hersteller_view, Geraetetyp, Hersteller, Barcodeelement

# Create your views here.


def devicemanagerappindex(request):
    return render(request, 'devicemanagerapp/devicemanagerappindex.html')


def hersteller_erstellen(request):
    # Hole die URL der vorherigen Seite, falls verfügbar
    previous_url = request.META.get('HTTP_REFERER', None)

    if request.method == 'POST':
        form = HerstellerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Hersteller wurde erfolgreich erstellt.")
            return redirect('hersteller_erstellen')  # Weiterleitung nach Erfolg
    else:
        form = HerstellerForm()
    
    # Render das Template und übergebe die previous_url
    return render(request, 'devicemanagerapp/hersteller_erstellen.html', {'form': form, 'previous_url': previous_url})


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
        geraete = Geraetetyp.objects.filter(
            Q(modellbezeichnung__icontains=query) |
            Q(herstellerid__name__icontains=query)
            ).select_related('herstellerid')  # Suche in der Modellbezeichnung

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

def delete_geraetetyp(request, geraetetypid):
    geraetetyp = get_object_or_404(Geraetetyp, geraetetypid=geraetetypid)
    if request.method == 'POST':
        geraetetyp.delete()
        messages.success(request, f"Gerätetyp {geraetetyp.modellbezeichnung} wurde erfolgreich gelöscht!")
        return redirect('geraete_liste')  # Zurück zur Geräte-Liste
    return redirect('geraete_liste')

def generate_barcodes(request, geraetetypid):
    # Sicherstellen, dass der Gerätetyp existiert
    geraetetyp = get_object_or_404(Geraetetyp, geraetetypid=geraetetypid)

    if request.method == 'POST':
        form = BarcodeelementForm(request.POST)
        try:
            # Anzahl der Barcodeelemente aus dem Formular abrufen
            anzahl = int(request.POST.get('anzahl', 1))
        except ValueError:
            messages.error(request, "Bitte geben Sie eine gültige Anzahl ein.")
            return redirect(request.path)

        if form.is_valid():
            # Barcodeelemente erstellen
            for i in range(anzahl):
                barcode = Barcodeelement(
                    geraetetypid=geraetetyp,
                    kaufdatum=form.cleaned_data.get('kaufdatum'),
                    bemerkungen=form.cleaned_data.get('bemerkungen'),
                    zustand=form.cleaned_data.get('zustand'),
                    länge=form.cleaned_data.get('länge'),
                    breite=form.cleaned_data.get('breite'),
                    höhe=form.cleaned_data.get('höhe'),
                    istgruppe=0  # `istgruppe` immer False setzen
                )
                barcode.save()

            messages.success(request, f"{anzahl} Barcodeelemente erfolgreich erstellt!")
            return redirect('geraete_liste')  # Weiterleitung zur Geräte-Liste
        else:
            messages.error(request, "Es gab ein Problem mit den eingegebenen Daten.")
    else:
        form = BarcodeelementForm()

    return render(request, 'devicemanagerapp/generate_barcode.html', {
        'form': form,
        'geraetetyp': geraetetyp,
    })

def barcodes_liste(request):
    query = request.GET.get('q', '')  # Suchparameter aus der URL abrufen

    if query:
        # Suche in Barcode, Modellbezeichnung und Hersteller
        barcodes = Barcodeelement.objects.filter(
            Q(barcode__icontains=query) |
            Q(geraetetypid__modellbezeichnung__icontains=query) |
            Q(geraetetypid__herstellerid__name__icontains=query)
        ).select_related('geraetetypid').order_by('barcode')
    else:
        # Ohne Suchbegriff alle Barcodes laden
        barcodes = Barcodeelement.objects.select_related('geraetetypid').order_by('barcode')

    return render(request, 'devicemanagerapp/barcodes_liste.html', {'barcodes': barcodes, 'query': query})


def barcode_details(request, barcode_id):
    # Barcode-Element basierend auf der ID abrufen
    barcode = get_object_or_404(Barcodeelement, barcode=barcode_id)
    return render(request, 'devicemanagerapp/barcode_details.html', {'barcode': barcode})

def edit_barcode(request, barcode_id):
    barcode = get_object_or_404(Barcodeelement, barcode=barcode_id)  # Barcode abrufen
    if request.method == 'POST':
        form = BarcodeelementForm(request.POST, instance=barcode)
        if form.is_valid():
            form.save()
            messages.success(request, "Barcode wurde erfolgreich aktualisiert!")
            return redirect('barcode_details', barcode_id=barcode.barcode)  # Zurück zur Detailansicht
    else:
        form = BarcodeelementForm(instance=barcode)
    return render(request, 'devicemanagerapp/edit_barcode.html', {'form': form, 'barcode': barcode})


def delete_barcode(request, barcode_id):
    barcode = get_object_or_404(Barcodeelement, barcode=barcode_id)
    if request.method == 'POST':
        barcode.delete()
        messages.success(request, f"Barcode {barcode_id} wurde erfolgreich gelöscht!")
        return redirect('barcodes_liste')  # Zurück zur Liste aller Barcodes
    return render(request, 'devicemanagerapp/delete_barcode.html', {'barcode': barcode})


# Auswahl des Zustands
def select_status(request):
    if request.method == 'POST':
        form = ZustandSelectionForm(request.POST)
        if form.is_valid():
            zustand = form.cleaned_data['zustand']
            # Speichere den ausgewählten Zustand in der Session
            request.session['selected_zustand'] = zustand
            return redirect('update_status')
    else:
        form = ZustandSelectionForm()

    return render(request, 'devicemanagerapp/select_status.html', {'form': form})

# Barcodeeingabe und Aktualisierung des Zustands
def update_status(request):
    selected_zustand = request.session.get('selected_zustand')
    if not selected_zustand:
        messages.error(request, "Bitte wählen Sie zuerst einen Zustand.")
        return redirect('select_status')

    if request.method == 'POST':
        form = BarcodeSingleInputForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']  # Der Barcode ist jetzt eine Zahl
            try:
                # Barcode aktualisieren
                barcode_element = Barcodeelement.objects.get(barcode=barcode)
                barcode_element.zustand = selected_zustand
                barcode_element.save()
                messages.success(request, f"Barcode {barcode} erfolgreich auf '{selected_zustand}' aktualisiert.")
            except Barcodeelement.DoesNotExist:
                messages.warning(request, f"Barcode {barcode} nicht gefunden.")

            # Zur Barcodeeingabe zurückkehren
            return redirect('update_status')
    else:
        form = BarcodeSingleInputForm()

    return render(request, 'devicemanagerapp/update_status.html', {
        'form': form,
        'selected_zustand': selected_zustand
    })
