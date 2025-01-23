from django import forms
from gestionvencimientos.models import Actividad

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre', 'dias_urbano', 'dias_rural', 'encargado']
