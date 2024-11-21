from django import forms
from .models import Kunde, Events

class KundeForm(forms.ModelForm):
    class Meta:
        model = Kunde
        fields = ['name', 'email', 'telefon', 'mobil', 'strassehausnummer', 'plz', 'stadt', 'notizen']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control'}),
            'mobil': forms.TextInput(attrs={'class': 'form-control'}),
            'strassehausnummer': forms.TextInput(attrs={'class': 'form-control'}),
            'plz': forms.TextInput(attrs={'class': 'form-control'}),
            'stadt': forms.TextInput(attrs={'class': 'form-control'}),
            'notizen': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'name': 'Name',
            'email': 'E-Mail',
            'telefon': 'Telefonnummer',
            'mobil': 'Mobilnummer',
            'strassehausnummer': 'Straße und Hausnummer',
            'plz': 'Postleitzahl',
            'stadt': 'Stadt',
            'notizen': 'Notizen',
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        # Alle Felder außer EventID einbeziehen
        exclude = ('eventid',)

def event_list(request):
    events = Events.objects.all()
    return render(request, 'event_list.html', {'events': events})

def edit_event(request, pk):
    event = get_object_or_404(Events, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Nach Bearbeitung zur Liste zurückkehren
    else:
        form = EventForm(instance=event)
    return render(request, 'edit_event.html', {'form': form})

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Events
        # Alle Felder außer KundenID, da wir sie im View setzen
        fields = ['eventortid', 'bezeichnung', 'startdatum', 'enddatum', 'notizen']

    # Optional: Customize Labels or Widgets
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['startdatum'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['enddatum'].widget = forms.DateInput(attrs={'type': 'date'})
