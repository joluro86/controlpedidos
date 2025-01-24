from django import forms
from gestionvencimientos.models import Actividad, Actividad_epm

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre', 'dias_urbano', 'dias_rural', 'encargado']

class ActividadEpmForm(forms.ModelForm):
    class Meta:
        model = Actividad_epm
        fields = ['nombre', 'dias_urbano', 'dias_rural']
