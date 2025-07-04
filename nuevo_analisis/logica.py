from django.shortcuts import redirect
from nuevo_analisis.factor_fm_con_cant_req import busqueda_pedidos_factor_multiple_con_cantidad_requerida
from nuevo_analisis.factor_fm_sin_cant_req import busqueda_pedidos_factor_multiple_sin_cantidad_requerida
from nuevo_analisis.logica_caracter import analisis_reglas_caracter
from nuevo_analisis.logica_duplicados import verificar_registros_duplicadas
from nuevo_analisis.logica_incompatibilidad import analisis_reglas_incompatibilidad
from nuevo_analisis.logica_limite_cantidad import analisis_reglas_limite_cantidad
from nuevo_analisis.logica_paginacion import verificar_paginacion
from nuevo_analisis.regla_fu_con_cant_req import busqueda_pedidos_factor_unico_con_cantidad_requerida
from nuevo_analisis.regla_fu_sin_cant_req import busqueda_pedidos_factor_unico_sin_cantidad_requerida

def analisis_reglas(request):

    verificar_paginacion()
    
    
    busqueda_pedidos_factor_unico_sin_cantidad_requerida()
    busqueda_pedidos_factor_unico_con_cantidad_requerida()

    busqueda_pedidos_factor_multiple_sin_cantidad_requerida()
    busqueda_pedidos_factor_multiple_con_cantidad_requerida()
    
    analisis_reglas_incompatibilidad()
    
    analisis_reglas_caracter()
    
    analisis_reglas_limite_cantidad()
    
    verificar_registros_duplicadas()
    

    return redirect('novedades_acta')



  

