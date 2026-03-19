# Sistema de inventario básico


# Lista para guardar los productos
inventario = []


# Función para agregar productos
def agregar_producto():
    print("\nAgregar producto")

    nombre = input("Nombre: ")

    # Validar precio
    while True:
        try:
            precio = float(input("Precio: "))
            break
        except ValueError:
            print("Ingrese un número válido.")

    # Validar cantidad
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            break
        except ValueError:
            print("Ingrese un número entero válido.")

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado.")


# Función para mostrar inventario
def mostrar_inventario():
    print("\nInventario:")

    if len(inventario) == 0:
        print("No hay productos.")
    else:
        for p in inventario:
            print(f"Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")


# Función para calcular estadísticas
def calcular_estadisticas():
    print("\nEstadísticas:")

    if len(inventario) == 0:
        print("Inventario vacío.")
    else:
        total = 0
        cantidad_total = 0

        for p in inventario:
            total += p["precio"] * p["cantidad"]
            cantidad_total += p["cantidad"]

        print(f"Valor total: {total}")
        print(f"Cantidad total de productos: {cantidad_total}")

# Menú principal
opcion = ""

while opcion != "4":
    print("\n1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        calcular_estadisticas()
    elif opcion == "4":
        print("Fin del programa")
    else:
        print("Opción inválida")

