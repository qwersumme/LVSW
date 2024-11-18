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
        fields = ['herstellerid', 'modellbezeichnung', 'kategorie', 'kaufpreis', 'notizen']
        widgets = {
            'herstellerid': forms.Select(attrs={'class': 'form-control'}),
            'modellbezeichnung': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modellbezeichnung'}),
            'kategorie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kategorie'}),
            'kaufpreis': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preis'}),
            'notizen': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notizen'}),
        }

 #   def __init__(self, *args, hersteller=None, **kwargs):
 #       super().__init__(*args, **kwargs)
 #       if hersteller:
 #           self.fields['hersteller']= forms.ModelChoiseField (
 #               queryset=Hersteller.objects.filter(pk=hersteller.pk),
 #               initial=hersteller,
 #               #widget=forms.HiddenInput()
 #           )

    def clean_modellbezeichnung(self):
        modellbezeichnung = self.cleaned_data.get('modellbezeichnung')
        if not modellbezeichnung:
            raise forms.ValidationError('Die Modellbezeichnung ist erforderlich.')
        return modellbezeichnung
