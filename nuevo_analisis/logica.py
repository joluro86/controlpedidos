from django.shortcuts import redirect
from nuevo_analisis.regla_fu_con_cant_req import busqueda_pedidos_factor_unico_con_cantidad_requerida
from nuevo_analisis.regla_fu_sin_cant_req import busqueda_pedidos_factor_unico_sin_cantidad_requerida

def analisis_reglas(request):

    busqueda_pedidos_factor_unico_sin_cantidad_requerida()
    busqueda_pedidos_factor_unico_con_cantidad_requerida()

    return redirect('novedades_acta')



  

