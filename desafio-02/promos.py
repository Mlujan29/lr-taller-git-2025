## Este archivo se usa para hacer un calculo de cada promocion

def calcular_descuento(items_de_venta,productos,promociones):
    descuento_total =  0                #acuulador para calcular el descuento total

    items_dict =  {}        #modificacion: para un recorrido mas sencillo hacemos que la lista que viene se convierta en diccionario
    for (codigo, cantidad) in items_de_venta:
        items_dict[codigo] = cantidad

    for promo in promociones:       #analizamos las promociones
        
        tipo_promo = promo['tipo']      # estandarizamos
        prod_promo = promo.get('producto')  #para cuando es un solo producto  (si hay más se guarda como NONE)
        
        if tipo_promo == "3x2":    # modificación: se adapto para el uso del diccionario y la estandarización
            if prod_promo in items_dict:    #si esta en el diccionario
                
                cantidad_vendida = items_dict[prod_promo]       #el valor de la clave en este caso es la cantidad
                cantidad_gratis = cantidad_vendida // 3     # usamos // para que sea entero el resultado
                descuento_total += cantidad_gratis * productos[prod_promo]['precio']
        
        elif tipo_promo == "10%":       # modificación: se adapto para el uso del diccionario y la estandarización
            if prod_promo in items_dict:
                
                cantidad_vendida = items_dict[prod_promo]
                if cantidad_vendida >= promo['min_cantidad']:               # Aca usamos 'min_cantidad' directo del diccionario de promociones
                    monto_producto = cantidad_vendida * productos[prod_promo]['precio']
                    descuento_total += monto_producto * 0.10   #se aplica el 10%

        elif tipo_promo == "combo_fijo":
            lista_combo = promo['productos'] # Lee ['galleta', 'cafe'] del diccionario de promocion
            
            p1 = lista_combo[0]
            p2 = lista_combo[1]
            
            if p1 in items_dict and p2 in items_dict:
                descuento_total += promo['descuento']   #ve cuanto se tiene que descontar
    
    return int(descuento_total)     #devolvemos el resultado final de descuento