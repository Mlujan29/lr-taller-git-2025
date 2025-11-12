#Implementa un CLI que lea comandos desde stdin (uno por línea) hasta recibir FIN. El sistema debe mantener 
# un inventario en memoria y un registro de ventas.


#       FUNCIONES
def alta(cod,descripcion,precio,productos):
    productos[cod] = {"descripcion": descripcion, "precio": precio, "stock": 0}
    print(f"OK: ALTA {productos}")


def stock(cod, cantidad, productos):
    if cod in productos:                            #verifica que el codigo ingresado exista
        productos[cod]["stock"] += cantidad
        if cantidad > 0:
            print(f"OK: STOCK {cod} --> +{cantidad}")
        else:
            print(f"OK: STOCK {cod} --> -{cantidad}")
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
                    precio =  int(partes[3])
                    alta(cod,descripcion,precio,productos)
                else:
                    print("ERROR: Ingrese el formato correcto para dar alta al producto")
            case "STOCK":
                if len(partes) == 3:    #validación en caso de que no se ingrese en el formato correcto
                    cod = partes[1]
                    cantidad = int(partes[2])
                    stock(cod,cantidad,productos)
                else:
                    print("ERROR: Ingrese el formato correcto para dar alta al producto")
            case "VENDE":
                if len(partes) == 3:    #validación en caso de que no se ingrese en el formato correcto
                    cod = partes[1]
                    cantidad = int(partes[2])
                    vende(cod,cantidad,productos,movimientos)
                else:
                    print("ERROR: Ingrese el formato correcto para dar alta al producto")
            case "DEVUELVE":
                print("aca va la funcion")
            case "REPORTE":
                print("aca va la funcion")
            case "FIN":
                print("Gracias por usar el programa! Adiós...")
                break
            case _:
                print("ERROR: Ingrese una entrada válida")
    else:
        print("ERROR: No se ingresó nada")