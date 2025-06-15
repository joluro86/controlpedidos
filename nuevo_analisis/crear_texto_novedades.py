def crear_texto_novedad(regla):
    if regla.comparador=="igual_a":
        novedad= f"{regla.objeto.nombre} {regla.item_busqueda} cobro diferente de {regla.cantidad}"
            
    if regla.comparador=="mayor_a":
        novedad= f"{regla.objeto.nombre} {regla.item_busqueda} menor igual a {regla.cantidad}"
                
    if regla.comparador=="menor_a":
        novedad= f"{regla.objeto.nombre} {regla.item_busqueda} mayor igual a {regla.cantidad}"

    return novedad  