from django import forms
from .models import Hersteller, Geraetetyp

class HerstellerForm(forms.ModelForm):
    class Meta:
        model = Hersteller
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Herstellername'}),
        }


class GeraetetypForm(forms.ModelForm):
    class Meta:
        model = Geraetetyp
        fields = ['herstellerid', 'modellbezeichnung', 'kategorie', 'anleitungslink', 'gewicht', 'laenge','breite','hoehe','kaufpreis', 'vermietpreis', 'mengenrabatt','zubehoer','notizen']
        widgets = {
            'herstellerid': forms.Select(attrs={'class': 'form-control'}),
            'modellbezeichnung': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PS-1801 MK2'}),
            'kategorie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sound'}),
            'anleitungslink': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'https://example.link/manual.pdf'}),
            'gewicht': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '40kg'}),
            'laenge': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '610mm'}),
            'breite': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '500mm'}),
            'hoehe': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '560mm'}),
            'kaufpreis': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '3000€'}),
            'vermietpreis': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '35,80 €'}),
            'mengenrabatt': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '10%'}),
            'zubehoer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'TV-Zapfen'}),
            'notizen': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notizen'}),
        }

    def clean_modellbezeichnung(self):
        modellbezeichnung = self.cleaned_data.get('modellbezeichnung')
        if not modellbezeichnung:
            raise forms.ValidationError('Die Modellbezeichnung ist erforderlich.')
        return modellbezeichnung
