from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Kunde, Events
from .forms import KundeForm, EventForm, EventCreateForm
# Create your views here.


def customermanagementapp(request):
    return render(request, 'customermanagementapp/customermanagementappindex.html')

def kunden_liste(request):
    query = request.GET.get('q', '')  # Suchparameter aus der URL abrufen
    if query:
        kunden = Kunde.objects.filter(
            name__icontains=query
        ) | Kunde.objects.filter(
            email__icontains=query
        ) | Kunde.objects.filter(
            telefon__icontains=query
        ) | Kunde.objects.filter(
            mobil__icontains=query
        ) | Kunde.objects.filter(
            stadt__icontains=query
        ) | Kunde.objects.filter(
            plz__icontains=query
        )
    else:
        kunden = Kunde.objects.all()

    return render(request, 'customermanagementapp/kunden_liste.html', {'kunden': kunden, 'query': query})

def kunde_erstellen(request):
    if request.method == 'POST':
        form = KundeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Kunde wurde erfolgreich erstellt.")
            return redirect('kunden_liste')  # Weiterleitung zur Kundenliste
    else:
        form = KundeForm()

    return render(request, 'customermanagementapp/kunde_erstellen.html', {'form': form})

def event_list(request):
    events = Events.objects.all()
    return render(request, 'customermanagementapp/event_list.html', {'events': events})

def edit_event(request, pk):
    event = get_object_or_404(Events, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Nach Bearbeitung zur Liste zurückkehren
    else:
        form = EventForm(instance=event)
    return render(request, 'customermanagementapp/edit_event.html', {'form': form})

def create_event(request, kundenid):
    # Überprüfe, ob die KundenID existiert
    kunde = get_object_or_404(Kunde, pk=kundenid)

    if request.method == 'POST':
        form = EventCreateForm(request.POST)
        if form.is_valid():
            # Form speichern, KundenID manuell setzen
            event = form.save(commit=False)
            event.kundenid = kunde  # Setze den Kunden
            event.save()
            return redirect('event_list')  # Zur Eventliste umleiten
    else:
        form = EventCreateForm()

    return render(request, 'customermanagementapp/create_event.html', {'form': form, 'kunde': kunde})
