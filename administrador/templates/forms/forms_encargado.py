from django import forms
from gestionvencimientos.models import Encargado

class EncargadoForm(forms.ModelForm):
    class Meta:
        model = Encargado
        fields = ['nombre']