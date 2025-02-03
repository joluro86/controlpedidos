from django import forms

from analisis_acta.models import VariableAnalisis
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

