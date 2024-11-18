from django import forms
from .models import Hersteller

class HerstellerForm(forms.ModelForm):
    class Meta:
        model = Hersteller
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Herstellername'}),
        }
