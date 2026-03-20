def agregar_producto(inventario):
    print("\nAgregar producto")

    nombre = input("Nombre del producto: ")

    # Validar precio
    continuar = True

    while continuar:
        try:
            precio = float(input("Precio: "))
            continuar = False
        except ValueError:
            print("Ingrese un número válido.")
            opcion = input("¿Quieres reintentarlo? si/no").lower()
            if opcion != "si":
                print("Operacion cancelada")
                return

    # Validar cantidad

    continuar = True

    while continuar:
        try:
            cantidad = int(input("Cantidad: "))
            continuar = False
        except ValueError:
            print("Ingrese un número entero válido.")
            opcion = input("¿Quieres reintentarlo? si/no").lower()
            if opcion != "si":
                print("Operacion cancelada")
                return

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado.")

def mostrar_inventario(inventario):
    print("\nInventario:")

    if len(inventario) == 0:
        print("No hay productos.")
    else:
        for p in inventario:
            print(f"Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")


# Función para calcular estadísticas
def calcular_estadisticas(inventario):
    print("\nEstadísticas:")

    if len(inventario) == 0:
        print("Inventario vacío.")
    else:
        total = 0
        cantidad_total = 0

        for  p in (inventario):
            total += p["precio"] * p["cantidad"]
            cantidad_total += 1
            print(f"La cantidad total es: {cantidad_total}")

        print(f"Valor total: {total}")
        print(f"Cantidad total de productos: {cantidad_total}")






