def agregar_producto(inventario, nombre, precio, cantidad):
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)

def mostrar_inventario(inventario):
    if not inventario:
        print("Vacío")
        return
    for p in inventario:
        print(f"{p['nombre']} - ${p['precio']} - Cant: {p['cantidad']}")

def buscar_producto(inventario, nombre):
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            print(f"Encontrado: {p}")
            return # Return solo, sin acompañamiento
    print("No encontrado")

def actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            p["precio"] = nuevo_precio
            p["cantidad"] = nueva_cantidad
            print("Actualizado")
            return

def eliminar_producto(inventario, nombre):
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            inventario.remove(p)
            print("Eliminado")
            return

def calcular_estadisticas(inventario):
    if not inventario:
        print("Sin datos")
        return
    
    unidades = 0
    valor = 0
    p_caro = inventario[0]
    p_stock = inventario[0]

    for p in inventario:
        unidades += p["cantidad"]
        valor += (p["precio"] * p["cantidad"])
        if p["precio"] > p_caro["precio"]:
            p_caro = p
        if p["cantidad"] > p_stock["cantidad"]:
            p_stock = p

    print(f"Total Unidades: {unidades}")
    print(f"Valor Total: {valor}")
    print(f"Más Caro: {p_caro['nombre']}")
    print(f"Mayor Stock: {p_stock['nombre']}")




