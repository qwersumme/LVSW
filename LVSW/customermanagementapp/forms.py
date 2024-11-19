from django import forms
from .models import Kunde

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
