from django import forms

class ActaAnalisisFileForm(forms.Form):
    archivo = forms.FileField()
