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



#   MAIN
productos =  {}     # Donde se van a almacenar los productos

PROMOCIONES = [                     # Definición de las promociones
    {
        'tipo': '3x2', 
        'producto': 'chicle'
    },
    {
        'tipo': '10%', 
        'producto': 'agua500', 
        'min_cantidad': 5
    },
    {
        'tipo': 'combo_fijo', 
        'productos': ['galleta', 'cafe'], 
        'descuento': 1000
    }
]

movimientos = []                # Registra los movimientos

while True:
    print("Acciones: ALTA, STOCK, VENDE, DEVUELVE, PROMOS, REPORTE, FIN")
    entrada = input("Realizar: ")

    if entrada.strip():     #verifica que la entrada no este vacia

        partes = entrada.split()
        match partes[0].upper():
            case "ALTA":
                if len(partes) == 4:    #validación en caso de que no se ingrese en el formato correcto
                    cod = partes[1]
                    descripcion = partes[2]

                    try:
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
                print("la funcion")

            case "VENDE":
                print("la funcion")

            case "DEVUELVE":
                print("la funcion")

            case "PROMOS":
                print("la funcion")

            case "REPORTE":
                print("la funcion")

            case "FIN":                            # cierra el programa
                print("Gracias por usar el programa! Adiós...")
                break

            case _:     # si se ingresa cualquier otra palabra
                print("Introduzca una acción válida")
    
    else:
        print("ERROR: No se ingresó nada")