
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from analisis_acta.models import CantidadItem

def crear_nueva_cantidad_item(request):
    if request.method == "POST":
        item = request.POST.get("item")
        cantidad = request.POST.get("cantidad")
        restriccion_tipo = request.POST.get("restriccion_tipo")

        # Crear el nuevo CantidadItem
        CantidadItem.objects.create(
            item=item,
            cantidad_cobro=cantidad,
            tipo_restriccion=restriccion_tipo
        )
        return redirect('index_admin')

    return render(request, 'nuevo_cantidad_item.html')


def lista_cantidad_items(request):
    cantidades = CantidadItem.objects.all()
    return render(request, "lista_cantidad_items.html", {"cantidades": cantidades})

def eliminar_cantidad_item(request, cantidad_id):
    if request.method == "POST":
        cantidad = get_object_or_404(CantidadItem, id=cantidad_id)
        cantidad.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False, "error": "Método no permitido"}, status=400)
