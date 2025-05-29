from django import forms
from .models import RelacionItemRegla, ItemRegla


class RelacionItemReglaForm(forms.ModelForm):
    item_requerido_nombre = forms.CharField(
        label='Item requerido',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = RelacionItemRegla
        fields = [
            'item',
            'requiere_cantidad',
            'cantidad_requeridad',
            'item_requerido_nombre',
            'tipo_requerido',            
            'cantidad',
            'comparador',
            'factor',
        ]
        widgets = {
            'item': forms.Select(attrs={'class': 'form-select'}),
            'requiere_cantidad': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cantidad_requeridad': forms.NumberInput(attrs={'class': 'form-control'}),
            'item_requerido': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),            
            'comparador': forms.Select(attrs={'class': 'form-select'}),
            'factor': forms.Select(attrs={'class': 'form-select'}),
        }

    def save(self, commit=True):
        relacion = super().save(commit=False)
        nombre_requerido = self.cleaned_data['item_requerido_nombre'].strip()

        item_requerido, _ = ItemRegla.objects.get_or_create(
            nombre=nombre_requerido,
            defaults={'tipo': relacion.item.tipo}
        )
        relacion.item_requerido = item_requerido

        if commit:
            relacion.save()
        return relacion


class ItemReglaForm(forms.ModelForm):
    class Meta:
        model = ItemRegla
        fields = ['nombre', 'tipo']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-select'
            }),

        }
