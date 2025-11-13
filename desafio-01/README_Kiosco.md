# Mini caja de Kiosco


##  Validaciones implementadas
1. Entrada Vacía: El programa ignora líneas vacías o con solo espacios (if entrada.strip()).
2. Formato de Comando: Se valida el número de argumentos para cada comando (ej. if len(partes) == 4 para ALTA). Si no coincide, muestra un error.
3. ALTA: El precio ingresado debe ser un número positivo (precio > 0).
4. VENDE:
    La cantidad a vender debe ser positiva (cantidad > 0).
    No se puede vender más de lo que hay en stock (cantidad <= productos[cod]["stock"]).
5. DEVUELVE: La cantidad a devolver debe ser positiva (cantidad > 0).
6. STOCK / VENDE / DEVUELVE: Todos estos comandos verifican que el cod del producto exista en el diccionario productos (if cod in productos) antes de operar.
7. Comando Desconocido: Si el primer argumento no coincide con ninguna de las acciones válidas, un case _: captura el error y muestra "ERROR: Ingrese una entrada válida".


####    Ejemplo de entrada:
ALTA 101 CocaCola 5000
ALTA 202 Chipa 3000
STOCK 101 50
STOCK 202 30
VENDE 202 10
REPORTE

###     Salida del ejemplo:
-------------------Caja de Kiosco-------------------
OK: ALTA 101 - CocaCola
OK: ALTA 202 - Chipa
OK: STOCK 101 --> +50
OK: STOCK 202 --> +30
OK: VENDE 202 --> 10 x 3000 = 30000

--------------------------------------------------
CODIGO     DESCRIPCION           PRECIO   STOCK
--------------------------------------------------
202       Chipa                 3000      20
    Ventas:     unidades: 10    monto: Gs 30000
    Devols:     unidades: 0     monto: Gs 0
Neto: 30000
.................................................
TOTAL EN CAJA: 45000
..................................................

Gracias por usar el programa! Adiós...