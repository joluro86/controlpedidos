from .models import ItemRegla
from django import forms
from .models import RelacionItemRegla, ItemRegla


class RelacionItemReglaForm(forms.ModelForm):
    item_requerido_nombre = forms.CharField(
        label='Item requerido',
        help_text='Nombre del ítem requerido. Se creará si no existe.',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = RelacionItemRegla
        fields = ['item', 'item_requerido_nombre',
                  'comparador', 'tipo_requerido', 'cantidad', 'factor']
        widgets = {
            'item': forms.Select(attrs={'class': 'form-select'}),
            'comparador': forms.Select(attrs={'class': 'form-select'}),
            'tipo_requerido': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'factor': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

    def save(self, commit=True):
        relacion = super().save(commit=False)
        nombre_requerido = self.cleaned_data['item_requerido_nombre'].strip()

        # Buscar o crear el ítem requerido
        item_requerido, creado = ItemRegla.objects.get_or_create(
            nombre=nombre_requerido,
            # Usa el mismo tipo del ítem principal
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
                'class': 'form-control',
                'placeholder': 'Ej. A47, 200492...'
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-select'
            }),

        }
