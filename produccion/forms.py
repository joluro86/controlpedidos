from django import forms
from .models import Valor_referencia

class ImportDataForm(forms.Form):
    Archivo_de_datos = forms.FileField()

class ValorReferenciaForm(forms.ModelForm):
    class Meta:
        model = Valor_referencia
        fields = ['valor']
        labels = {'valor': 'Nuevo Valor'}