# your_app_name/forms.py
from django import forms
from nuevo_analisis.models import ItemRegla, RelacionItemRegla # Asegúrate de que 'nuevo_analisis' sea la ruta correcta o usa '.'

class ItemReglaForm(forms.ModelForm):
    class Meta:
        model = ItemRegla
        fields = ['nombre', 'tipo']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '200410'
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
        labels = {
            'nombre': 'Nombre del Ítem',
            'tipo': 'Tipo de Ítem',
        }
        help_texts = {
            'nombre': 'Ingrese el nombre del ítem de regla.',
            'tipo': 'Seleccione la categoría principal del ítem.',
        }
class RelacionItemReglaForm(forms.ModelForm):
    class Meta:
        model = RelacionItemRegla
        fields = [
            'objeto',
            'requiere_cantidad',
            'cantidad_condicion',
            'factor',
            'tipo_item_busqueda',
            'item_busqueda',
            'conjuncion', # Asegurarse de que esté aquí
            'comparador',
            'cantidad'
        ]
        widgets = {
            'objeto': forms.Select(attrs={
                'class': 'form-select'
            }),
            'requiere_cantidad': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'cantidad_condicion': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad necesaria para la condición',
                'min': '1'
            }),
            'factor': forms.Select(attrs={
                'class': 'form-select'
            }),
             'tipo_item_busqueda': forms.Select(attrs={
                'class': 'form-select'
            }),
            'item_busqueda': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'conjuncion': forms.Select(attrs={ # Asegurarse de que esté aquí
                'class': 'form-select'
            }),
            'comparador': forms.Select(attrs={
                'class': 'form-control' # Aunque es un select, a veces 'form-control' funciona para select en Bootstrap 5, pero 'form-select' es más específico. Me mantengo con 'form-select' para consistencia.
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad',
                'min': '1'
            }),
        }
        labels = {
            'objeto': 'Item a relacionar',
            'requiere_cantidad': '¿Depende de una Cantidad Específica del Objeto?',
            'cantidad_condicion': 'Cantidad del Objeto para Aplicar la Regla',
            'factor': 'Factor de la Relación',
            'item_busqueda': 'Código(s) Ítem(s) Asociado(s)', # Ajuste de label para ser más preciso
            'conjuncion': 'Relación de Búsqueda', # Label más descriptivo
            'comparador': 'Condición de Comparación',
            'cantidad': 'Cantidad del Ítem Asociado Requerida',
        }
        help_texts = {
            'item_busqueda': 'Separe con comas si es multiple (ej. 200410,200411).',
            'conjuncion': 'Indica si se deben cumplir "Todos" los ítems o "Uno".', # Help text para conjuncion
            'comparador': 'Establece cómo se compara la cantidad',
            'cantidad': 'Ingrese la cantidad para cumplir la condición.',
        }