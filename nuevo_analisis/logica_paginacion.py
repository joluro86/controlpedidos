from analisis_acta.models import Acta
from analisis_acta.views import crear_novedad

def verificar_paginacion():
    # Solo traemos los campos necesarios para evaluar y evitar traer toda la tabla
    pedidos = (
        Acta.objects
        .values('id', 'pedido', 'pagina', 'urbrur')
        .distinct()
    )

    for p in pedidos:
        pagina = p.get('pagina') or ''
        urbrur = p.get('urbrur')
        
        if len(pagina) >= 9:
            codigo = pagina[6:9]
            if (codigo == '100' and urbrur != 'U') or (codigo == '200' and urbrur != 'R'):
                try:
                    acta = Acta.objects.get(id=p['id'])  # Buscamos el objeto real por ID
                    crear_novedad(acta, f"Incompatibilidad: código {codigo} con zona {urbrur}")
                except Acta.DoesNotExist:
                    pass
