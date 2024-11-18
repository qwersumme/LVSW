from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import HerstellerForm
from .models import Hersteller_view

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


