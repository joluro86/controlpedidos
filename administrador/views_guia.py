from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.shortcuts import redirect
from administrador.forms import GuiaForm
from administrador.query.actividades.guias import actualizar_guia_id, eliminar_guia_id, existencia_equivalencia
from perseovsfenix.models import Guia
from django.contrib import messages
from django.http import JsonResponse

class GuiaListView(ListView):
    model = Guia
    template_name = 'guia_list.html'  # Nombre del template a renderizar
    context_object_name = 'guias'  # Nombre de la variable en el template

class GuiaCreateView(CreateView):
    model = Guia
    form_class = GuiaForm
    template_name = 'nueva_guia.html'
    success_url = reverse_lazy('index_admin')
    
    def form_valid(self, form):
        nombre_per = form.cleaned_data['nombre_perseo']

        # Verificar si ya existe una guía con estos valores
        if existencia_equivalencia(nombre_per):
            messages.success(self.request, "La equivalencia ya existe. No se puede duplicar.")
            return redirect('index_admin')  # Redirige a la misma página o a donde prefieras

        response = super().form_valid(form)
        messages.success(self.request, "Equivalencia creada exitosamente.")
        return response
    
def actualizar_guia(request, id):
    if request.method == 'POST':
        try:
            if actualizar_guia_id(request, id):
                return JsonResponse({'success': True})
        except Guia.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Equivalencia no existe'})
    return JsonResponse({'success': False, 'error': 'Revisar posible equivalencia duplicada.'})
    
def eliminar_guia(request,id):
    eliminar_guia_id(id)
    return redirect('index_admin')
    
    
    