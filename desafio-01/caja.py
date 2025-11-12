#Implementa un CLI que lea comandos desde stdin (uno por línea) hasta recibir FIN. El sistema debe mantener 
# un inventario en memoria y un registro de ventas.

def alta(cod,descripcion,precio,productos):
    productos[cod] = {"descripcion": descripcion, "precio": precio, "stock": 0}
    print(f"OK: ALTA {productos}")


productos = {}

print("-------------------Caja de Kiosco-------------------")
while True:
    print("Acciones: ALTA, STOCK, VENDE, DEVUELVE, REPORTE, FIN")
    entrada = input("Realizar: ")
    if entrada.strip():
        partes = entrada.split()
        match partes[0].upper():
            case "ALTA":
                if len(partes) == 4:
                    cod = partes[1]
                    descripcion = partes[2]
                    precio =  partes[3]
                    alta(cod,descripcion,precio, productos)
                else:
                    print("ERROR: Ingrese el formato correcto para dar alta al producto")
            case "STOCK":
                print("funcion")
            case "VENDE":
                print("aca va la funcion")
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