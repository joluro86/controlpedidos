from django.shortcuts import render

from sellos.models import ActaSello, MaterialInstalado, SerieSello


def pedidos_de_instalado_a_series(request):
    series = SerieSello.objects.all()
    cont=1
    for serie in series:
        
        if MaterialInstalado.objects.filter(consecutivo=serie.consecutivo).exists():
            serie.pedido = MaterialInstalado.objects.filter(consecutivo=serie.consecutivo).first().pedido
            
            if ActaSello.objects.filter(pedido=serie.pedido).exists():
                serie.va_en_informe= True
                print(cont)
                cont+=1
                
            serie.save()
            
            
            
            
        