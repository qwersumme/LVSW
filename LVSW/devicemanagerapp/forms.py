from django import forms
from .models import Hersteller, Geraetetyp, Barcodeelement, Gruppe

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
            'kategorie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sound/Mischpult'}),
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

    labels = {
        'herstellerid': 'Hersteller',
    }  

    def clean_modellbezeichnung(self):
        modellbezeichnung = self.cleaned_data.get('modellbezeichnung')
        if not modellbezeichnung:
            raise forms.ValidationError('Die Modellbezeichnung ist erforderlich.')
        return modellbezeichnung

class BarcodeelementForm(forms.ModelForm):

    ZUSTAND_CHOICES = [
        ('Frei', 'Frei'),
        ('Verliehen', 'Verliehen'),
        ('Ausgemustert', 'Ausgemustert'),
        ('Defekt', 'Defekt'),
        ('Reparatur', 'Reparatur'),
        ('Gesperrt', 'Gesperrt'),
    ]
    zustand = forms.ChoiceField(
        choices=ZUSTAND_CHOICES, 
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}), 
        )  # Auswahlfeld

    class Meta:
        model = Barcodeelement
        fields = ['kaufdatum', 'bemerkungen', 'zustand', 'länge', 'breite', 'höhe']
        widgets = {
            'kaufdatum': forms.DateInput(
                format='%d.%m.%Y', 
                attrs={'class': 'form-control', 'placeholder':'mm/dd/yyyy'}),
            'bemerkungen': forms.Textarea(attrs={'class': 'form-control','rows': 3, 'placeholder': 'Notizen'}),
            'zustand': forms.Select(attrs={'class': 'form-control'}),
            'länge': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '610mm'}),

            'breite': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '500mm'}),
            'höhe': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '560mm'}),
        }

class BarcodeelementForm2(forms.ModelForm):
    class Meta:
        model = Barcodeelement
        fields = [
            'kaufdatum', 'bemerkungen', 'istgruppe', 
            'zustand', 'länge', 'breite', 'höhe'
        ]
        input_formats=['%d.%m.%Y']
        widgets = {
            'kaufdatum': forms.DateInput(format='%d.%m.%y', attrs={'type': 'date', 'class': 'form-control'}),
            'bemerkungen': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'zustand': forms.Select(attrs={'class': 'form-control'}),
            'länge': forms.NumberInput(attrs={'class': 'form-control'}),
            'breite': forms.NumberInput(attrs={'class': 'form-control'}),
            'höhe': forms.NumberInput(attrs={'class': 'form-control'}),
            'istgruppe': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    labels = {
        'kaufdatum': 'Kaufdatum',
        'bemerkungen': 'Bemerkungen',
        'istgruppe': 'Ist Gruppe',
        'zustand': 'Zustand',
        'länge': 'Länge (cm)',
        'breite': 'Breite (cm)',
        'höhe': 'Höhe (cm)',
    }

# Formular zur Auswahl des Zustands
class ZustandSelectionForm(forms.Form):
    ZUSTAND_CHOICES = [
        ('Frei', 'Frei'),
        ('Verliehen', 'Verliehen'),
        ('Ausgemustert', 'Ausgemustert'),
        ('Defekt', 'Defekt'),
        ('Reparatur', 'Reparatur'),
        ('Gesperrt', 'Gesperrt'),
    ]
    zustand = forms.ChoiceField(choices=ZUSTAND_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

# Formular zur Eingabe eines einzelnen Barcodes als Zahl
class BarcodeSingleInputForm(forms.Form):
    barcode = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Barcode eingeben...',
            'min': 1  # Optional: Mindestwert
        }),
        label="Barcode"
    )

class GruppeForm(forms.Form):
    gruppen_barcode = forms.ModelChoiceField(
        queryset=Barcodeelement.objects.all(),
        label="Gruppen-Barcode",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    barcodes = forms.ModelMultipleChoiceField(
        queryset=Barcodeelement.objects.all(),
        label="Barcodes zur Gruppe hinzufügen",
        widget=forms.CheckboxSelectMultiple
    )
    

class GruppenErstellForm(forms.Form):
    name = forms.CharField(
    max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name eingeben'}),
    label="Name"
    )