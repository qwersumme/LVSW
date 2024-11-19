from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Kunde
from .forms import KundeForm
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

