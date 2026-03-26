# Proyecto
Sistema de Inventario
Aplicación de consola en Python para gestionar un inventario de productos. Permite agregar, buscar, actualizar y eliminar productos, calcular estadísticas, y guardar o cargar datos en formato CSV.

Requisitos

Python 3.x
No requiere librerías externas


Estructura del proyecto
proyecto/
├── app.py          # Menú principal y flujo del programa
├── servicios.py    # Lógica del inventario (agregar, buscar, actualizar, eliminar, estadísticas)
├── archivos.py     # Lectura y escritura de archivos CSV
└── README.md       # Documentación del proyecto

Cómo ejecutar
bashpython app.py

Si no funciona, prueba con python3 app.py


Funcionalidades
OpciónDescripción1Agregar un nuevo producto2Mostrar todos los productos3Buscar un producto por nombre4Actualizar precio y cantidad de un producto5Eliminar un producto6Ver estadísticas del inventario7Guardar inventario en CSV8Cargar inventario desde CSV9Salir

Ejemplo de uso

Ejecutar el programa con python app.py
Seleccionar opción 1 para agregar un producto
Ingresar nombre, precio y cantidad
Seleccionar opción 2 para ver el inventario
Seleccionar opción 7 para guardar los datos en inventario.csv
Al salir con opción 9, el programa pregunta si desea guardar cambios pendientes


Validaciones

Precio y cantidad deben ser valores numéricos mayores a 0
Solo se permiten archivos con extensión .csv al cargar datos
Al salir, si hay cambios sin guardar el programa lo notifica


Archivos generados
Al guardar el inventario se crea el archivo inventario.csv en la misma carpeta del proyecto con el siguiente formato:
nombre,precio,cantidad
Manzana,1.5,10
Pera,2.0,5

Autor
Dylan Castillo
