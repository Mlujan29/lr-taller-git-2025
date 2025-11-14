#Implementa un CLI que lea comandos desde stdin (uno por línea) hasta recibir FIN. El sistema debe mantener 
# un inventario en memoria y un registro de ventas.


#       FUNCIONES
def alta(cod,descripcion,precio,productos):
    if cod in productos:                        #si el codigo ya existe (ya que debe de ser único)
        print("ALERTA: El codigo ya existía ¿Desea sobrescribirlo? El Stock volverá a cero")
        confirmación = input("[S/N]: ")         #guarda la respuesta
        if confirmación.upper() == 'S' or confirmación.upper() == "SI":
            productos[cod] = {"descripcion": descripcion, "precio": precio, "stock": 0}
            print(f"OK: ALTA {cod} - {descripcion}")
        elif confirmación.upper() == 'N' or confirmación.upper() == "NO":       #si dice que no vuelve al comienzo
            return
        else:                   #si ingresa cualquier otra cosa
            print("ERROR: La confirmación no fue válida")
    else:
        productos[cod] = {"descripcion": descripcion, "precio": precio, "stock": 0}
        print(f"OK: ALTA {cod} - {descripcion}")


def stock(cod, cantidad, productos):
    if cod in productos:                            #verifica que el codigo ingresado exista
        productos[cod]["stock"] += cantidad
        if cantidad > 0:
            print(f"OK: STOCK {cod} --> +{cantidad}")
        else:
            print(f"OK: STOCK {cod} --> {cantidad}")
    else:
        print("ERROR: El código ingresado no existe")


def vende(cod, cantidad, productos, movimientos):
    if cod in productos:
        if cantidad <= productos[cod]["stock"]:
            monto = cantidad * productos[cod]["precio"]
            print(f"OK: VENDE {cod} --> {cantidad} x {productos[cod]["precio"]} = {monto}")
            productos[cod]["stock"] -= cantidad
            movimientos.append({"Tipo": "VENTA", "Cod": cod, "Cantidad": cantidad, "Monto": monto})
        else:
            print("ERROR: No hay suficiente stock para la venta.")
            print(f"Disponible: {productos[cod]["stock"]}")
    else:
        print("ERROR: El código ingresado no existe")


def devuelve(cod, cantidad, productos, movimientos):
    if cod in productos:                            #verifica que el codigo ingresado exista
        monto_perdido = cantidad * productos[cod]["precio"] * (-1)
        print(f"OK: DEVUELVE {cod} --> {cantidad} x {productos[cod]["precio"]} = {monto_perdido}")
        productos[cod]["stock"] += cantidad
        movimientos.append({"Tipo": "DEVOLUCION", "Cod": cod, "Cantidad": cantidad, "Monto": monto_perdido})
    else:
        print("ERROR: El código ingresado no existe")


def reporte(movimientos, productos):
    print("--------------------------------------------------")
    print(f"{'CODIGO':<10} {'DESCRIPCION':<15} {'PRECIO':>10} {'STOCK':>7}")        #correción con comillas simples
    print("--------------------------------------------------")
    total = 0
    for codigo, item in productos.items():      #va a recorrer todos los productos que se dieron alta
        desc = item["descripcion"]
        precio = item["precio"]
        stock = item["stock"]
        
        #acumuladores
        cantVenta = 0
        cantDevo = 0
        montoVenta = 0
        montoDevo = 0

        for mov in movimientos:             #analizamos cada movimiento
            if mov["Cod"] == codigo:        #solo si el producto del primer bucle coincide con el que esta en la venta
                if mov["Tipo"] == "VENTA":
                    cantVenta += mov["Cantidad"]
                    montoVenta += mov["Monto"]
                elif mov["Tipo"] == "DEVOLUCION":
                    cantDevo += mov["Cantidad"]
                    montoDevo += mov["Monto"]
        neto = montoVenta+montoDevo                     #guardamos el monto generado por cada articulo
        total += neto                                   #lo ponemos en el total de la caja
        
        if neto != 0:       #solo vamos a mostrar los productos que se encontraron en venta
            print(f"{codigo:<10}{desc:<15}{precio:>10}{stock:>7}")
            print(f"    Ventas:     unidades: {cantVenta:<5} monto: Gs {montoVenta}")
            print(f"    Devols:     unidades: {cantDevo:<5} monto: Gs {montoDevo}")
            print(f"Neto: {neto}")
            print(".................................................""")
    print(f"TOTAL EN CAJA: {total}")
    print("..................................................""")


#       MAIN
productos = {}      # para uso general
movimientos = []    # para las ventas y devoluciones

print("-------------------Caja de Kiosco-------------------")
while True:
    print("Acciones: ALTA, STOCK, VENDE, DEVUELVE, REPORTE, FIN")
    entrada = input("Realizar: ")
    if entrada.strip():                 #Esta funcion sirve para ver si la entrada esta vacia o solo tiene espacios
        partes = entrada.split()        #Guardo en una lista los comandos ingresados por el usuario

        match partes[0].upper():    #comparamos el comando con cada caso
            case "ALTA":
                if len(partes) == 4:    #validación en caso de que no se ingrese en el formato correcto
                    cod = partes[1]
                    descripcion = partes[2]

                    try:    #modificación
                        precio =  int(partes[3])
                        if precio <= 0:                     #para rechazar la accion si el precio es negaivo o cero
                            print("ERROR: Ingrese un precio válido")
                        else:
                            alta(cod,descripcion,precio,productos)
                    except ValueError:
                        print("ERROR: El precio debe de ser un número")
                
                else:
                    print("ERROR: Ingrese el formato correcto para dar alta al producto")
            
            case "STOCK":
                if len(partes) == 3:    #validación en caso de que no se ingrese en el formato correcto
                    cod = partes[1]
                    
                    try:    #modificación
                        cantidad = int(partes[2])       #la cantidad si puede ser negativa, en caso de que algo le pase al stock ya definido
                        stock(cod,cantidad,productos)
                    except ValueError:
                        print("ERROR: La cantidad debe de ser un número")
                
                else:
                    print("ERROR: Ingrese el formato correcto para dar stock al producto")
            
            case "VENDE":
                if len(partes) == 3:    #validación en caso de que no se ingrese en el formato correcto
                    cod = partes[1]

                    try:
                        cantidad = int(partes[2])
                        if cantidad <= 0:                     #rechaza la accion si la cantidad es negativa o cero
                            print("ERROR: Ingrese una cantidad válida")
                        else:
                            vende(cod,cantidad,productos,movimientos)
                    except ValueError:
                        print("ERROR: La cantidad debe de ser un número")

                else:
                    print("ERROR: Ingrese el formato correcto para vender el producto")
            
            case "DEVUELVE":
                if len(partes) == 3:    #validación en caso de que no se ingrese en el formato correcto
                    cod = partes[1]
                    
                    try:
                        cantidad = int(partes[2])
                        if cantidad <= 0:                     #rechaza la accion si la cantidad es negativa o cero
                            print("ERROR: Ingrese una cantidad válida")
                        else:
                            devuelve(cod,cantidad,productos,movimientos)
                    except ValueError:
                        print("ERROR: La cantidad debe de ser un número")
                
                else:
                    print("ERROR: Ingrese el formato correcto para devolver el producto")
            
            case "REPORTE":
                reporte(movimientos,productos)
            
            case "FIN":
                print("Gracias por usar el programa! Adiós...")
                break
            
            case _:                                                     #si se ingresa cualquier otra palabra
                print("ERROR: Ingrese una entrada válida")
    
    else:
        print("ERROR: No se ingresó nada")