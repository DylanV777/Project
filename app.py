# Importación de módulos externos
from servicios import *
from archivos import *

# Variables de control de estado del programa
cambios_no_guardados = False
inventario = []
continuar = True

# Bucle principal que mantiene el menú activo
while continuar:
    print()
    print("-------------MENÚ-------------")
    print("\n1.Agregar producto \n2.Mostrar inventario \n3.Buscar producto \n4.Actualizar producto \n5.Eliminar producto \n6.Calcular estadísticas \n7.Guardar CSV \n8.Cargar CSV \n9.Salir")
    opcion = input("Opción: ")
    print()

# OPCIÓN 1: Registro de nuevos productos con validación independiente
    if opcion == "1":
        nombre = input("Nombre del producto: ")
        again = True
        while again:
            try:
                precio = float(input("Precio del producto: "))
                if precio > 0:
                    # Bucle interno para asegurar que la cantidad sea correcta sin volver al precio
                    cantidad_ok = False
                    while not cantidad_ok:
                        cantidad = int(input("Ingrese la cantidad: "))
                        if cantidad > 0:
                            agregar_producto(
                                inventario, nombre, precio, cantidad)
                            print("Producto agregado")
                            cambios_no_guardados = True
                            cantidad_ok = True
                            again = False  # Finaliza ambos bucles al tener éxito
                        else:
                            print("Ingrese valores positivos")
                else:
                    print("Ingrese un valor positivo")

            except ValueError:
                # Captura errores de tipo de dato (letras en lugar de números)
                print("Error en datos")
                again = input("¿Desea reintentarlo? si/no: ")
                if again.lower() == "no":
                    print("Operación cancelada")
                    again = False

# OPCIÓN 2: Listar todos los productos en memoria
    elif opcion == "2":
        mostrar_inventario(inventario)

# OPCIÓN 3: Localizar un producto por su nombre
    elif opcion == "3":
        buscar_producto(inventario, input("Nombre: "))

# OPCIÓN 4: Modificar precio y cantidad de un producto existente
    elif opcion == "4":
        nombre = input("Nombre: ")
        again = True
        while again:
            try:
                precio = float(input("Nuevo precio: "))
                if precio > 0:
                    cantidad_ok = False
                    while not cantidad_ok:
                        cantidad = int(input("Nueva cantidad: "))
                        if cantidad > 0:
                            actualizar_producto(
                                inventario, nombre, precio, cantidad)
                            cambios_no_guardados = True
                            cantidad_ok = True
                            again = False
                        else:
                            print("Ingrese un valor positivo")
                else:
                    print("Ingrese valores positivos")

            except ValueError:
                print("Error en datos")
                retry = input("¿Desea reintentarlo? si/no: ")
                if retry.lower() == "no":
                    print("Operación cancelada")
                    again = False

# OPCIÓN 5: Quitar un producto del inventario
    elif opcion == "5":
        if eliminar_producto(inventario, input("Nombre: ")):
            cambios_no_guardados = True

# OPCIÓN 6: Mostrar cálculos (totales, producto más caro, etc.)
    elif opcion == "6":
        calcular_estadisticas(inventario)

# OPCIÓN 7: Persistencia de datos hacia archivo CSV
    elif opcion == "7":
        guardar_csv(inventario)
        cambios_no_guardados = False

# OPCIÓN 8: Carga de datos desde archivo externo
    elif opcion == "8":
        productos_cargados = cargar_csv()
        inventario.extend(productos_cargados)
        cambios_no_guardados = False
        input("Presione ENTER para volver al menú...")

# OPCIÓN 9: Salida controlada con verificación de guardado pendiente
    elif opcion == "9":
        if cambios_no_guardados:
            guardar = input(
                "¿Quiere guardar cambios antes de salir? (S / cualquier otra tecla para NO): ")
            if guardar.upper() == "S":
                guardar_csv(inventario)
            else:
                print("Saliendo sin guardar...")
        else:
            print("Saliendo...")
        continuar = False
