# Desafío 02: Sistema de Caja para Kiosco

Este proyecto implementa un sistema de consola para la gestión de ventas, control de stock y aplicación de promociones en un kiosco. El diseño prioriza la modularización, separando la lógica de negocio (descuentos) de la gestión de estado (inventario y caja).

### Archivos

El programa consta de dos archivos principales:
1.  `caja.py`: El script principal que gestiona la entrada del usuario y el inventario.
2.  `promos.py`: Un módulo externo encargado exclusivamente de calcular descuentos.

### Supuestos
Para cumplir con los requerimientos y asegurar una experiencia de usuario lógica, se tomaron las siguientes decisiones de diseño:

1. Modelo de "Carrito de Compras":
Dado que existen promociones que dependen de la combinación de productos (ej. Combo Galleta + Café), se implementó un sistema de dos pasos:
    * VENDE <cod> <cant>: Añade productos a un "carrito" temporal y reserva el stock, pero no finaliza la transacción.
    * COBRAR: Cierra la venta, aplica los descuentos sobre el total del carrito, descuenta el stock real y genera el recibo.
    * El comando FIN o el cierre del programa descarta cualquier carrito no cobrado.

2. Validación de Stock:
El sistema valida la disponibilidad de stock en tiempo real al momento de añadir al carrito (VENDE). Si no hay suficiente stock para cubrir la suma de lo que ya está en el carrito más lo nuevo, la operación se rechaza.

3. Persistencia:
El sistema funciona en memoria. Todos los datos (inventario y reporte) se pierden al cerrar el programa (FIN).

4. Ordenamiento:
Para el reporte de "Top 3 Productos", si hay un empate en unidades vendidas, el orden entre ellos no es determinante.

###  Estructuras utilizadas
1. Diccionarios (dict)
Se utilizaron extensivamente por su eficiencia de acceso O(1) (búsqueda instantánea por clave).

    * Inventario (productos): {'codigo': {'precio': 100, 'stock': 10...}}. Permite acceder a la información de un producto rápidamente usando su código único.

    * Carrito (carrito): {'codigo': cantidad}. Permite acumular cantidades automáticamente si el usuario ingresa el mismo producto varias veces antes de cobrar.

2. Listas (list)
Se utilizaron donde el orden secuencial y cronológico es importante.

    * Historial (movimientos): Almacena cada transacción (VENTA o DEVOLUCION) en el orden exacto en que ocurrieron. Fundamental para auditar la caja y generar reportes.

    * Items de Venta: Dentro de cada movimiento, los productos vendidos se guardan como una lista de tuplas [(cod, cant), ...] para preservar el detalle de la factura.

3. Módulo Externo (promos.py)
Se separó la lógica de cálculo de descuentos para cumplir con el principio de Separación de Responsabilidades. El archivo principal no necesita saber cómo se calcula una promoción, solo le interesa el monto final del descuento.

### Ejemplo de entrada:
```text
ALTA cafe Cafe_Negro 5000
ALTA galleta Galleta_Vainilla 2500
STOCK cafe 10
STOCK galleta 10
VENDE cafe 1
VENDE galleta 1
COBRAR
REPORTE
FIN
```

### Ejemplo de salida:
```text        
-------------------Caja de Kiosco-------------------
OK: ALTA cafe - Cafe_Negro
OK: ALTA galleta - Galleta_Vainilla
OK: STOCK cafe --> +10
OK: STOCK galleta --> +10
-------------------------------------------
Para terminar ingrese: COBRAR
OK: VENDE cafe --> 1
-------------------------------------------
Para terminar ingrese: COBRAR
OK: VENDE galleta --> 1
La venta fue realizada con exito!

----------------------------REPORTE GENERAL----------------------------

--------------------  INVENTARIO --------------------
- cafe : {'descripcion': 'Cafe_Negro', 'precio': 5000, 'stock': 9}
- galleta : {'descripcion': 'Galleta_Vainilla', 'precio': 2500, 'stock': 9}
-----------------------------------------------------

TOTALES:
Ventas Brutas:         7500 Gs
Descuentos:            1000 Gs
Devoluciones:             0 Gs
---------------------------------
MONTO NETO:            6500 Gs

Los 3 productos más vendidos son:
Top 1: galleta - 1 unidades
Top 2: cafe - 1 unidades

--- FIN REPORTE ---
Gracias por usar el programa! Adiós...
```