from django import forms

from analisis_acta.models import VariableAnalisis
from perseovsfenix.models import Guia
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']
        
class VariableContratoForm(forms.ModelForm):
    class Meta:
        model = VariableAnalisis
        fields = ['region', 'contrato']
        # Si deseas agregar clases CSS a los widgets, puedes hacerlo aquí:
        widgets = {
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'contrato': forms.TextInput(attrs={'class': 'form-control'}),
        }

class GuiaForm(forms.ModelForm):
    class Meta:
        model = Guia
        fields = ['nombre_perseo', 'nombre_fenix']
        labels = {
            'nombre_perseo': 'Nombre en Perseo',
            'nombre_fenix': 'Nombre en Fénix',
        }
        widgets = {
            'nombre_perseo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_fenix': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        nombre_perseo = cleaned_data.get('nombre_perseo')

        if Guia.objects.filter(nombre_perseo=nombre_perseo).exists():
            raise forms.ValidationError("Esta equivalencia ya existe. No se puede duplicar.")

        return cleaned_data

