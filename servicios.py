# Función para agregar un nuevo producto al inventario
def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.
 
    Argumentos:
        inventario (list): Lista de productos existentes
        nombre (str): Nombre del producto
        precio (float): Precio del producto (debe ser mayor a 0)
        cantidad (int): Cantidad disponible (debe ser mayor a 0)
    """
    # Crear un diccionario con los datos del producto
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    # Agregar el producto a la lista de inventario
    inventario.append(producto)

# Función para mostrar todos los productos del inventario


def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario por consola.
 
    Argumentos:
        inventario (list): Lista de productos existentes
    """
    # Si el inventario está vacío, mostrar mensaje y salir
    if not inventario:
        print("Inventario vacío")
        return
    # Recorrer cada producto en el inventario e imprimir sus datos
    for p in inventario:
        print(f"{p['nombre']} - ${p['precio']} - Cantidad: {p['cantidad']}")

# Función para buscar un producto por nombre


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre y lo muestra si existe.
    La búsqueda no distingue entre mayúsculas y minúsculas.
 
    Argumentos:
        inventario (list): Lista de productos existentes
        nombre (str): Nombre del producto a buscar
    """
    # Comparar nombres sin importar mayúsculas/minúsculas
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            print(f"Encontrado: {p}")  # Mostrar producto encontrado
            return
    # Si no se encuentra ningún producto, mostrar mensaje
    print("Producto no encontrado")

# Función para actualizar precio y cantidad de un producto existente


def actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
    """
    Actualiza el precio y la cantidad de un producto existente.
    La búsqueda no distingue entre mayúsculas y minúsculas.
 
    Argumentos:
        inventario (list): Lista de productos existentes
        nombre (str): Nombre del producto a actualizar
        nuevo_precio (float): Nuevo precio del producto
        nueva_cantidad (int): Nueva cantidad del producto
    """
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            p["precio"] = nuevo_precio
            p["cantidad"] = nueva_cantidad
            print("Actualizado")
            return

    print("Producto no encontrado")

# Función para eliminar un producto del inventario


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario por nombre.
    La búsqueda no distingue entre mayúsculas y minúsculas.
 
    Argumentos:
        inventario (list): Lista de productos existentes
        nombre (str): Nombre del producto a eliminar
 
    Returns:
        bool: True si el producto fue eliminado, False si no existía
    """
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            inventario.remove(p)
            print("Eliminado")
            return True       
    print("El producto no existe")
    return False             

# Función para calcular estadísticas del inventario
def calcular_estadisticas(inventario):
    """
    Calcula y muestra estadísticas del inventario:
    total de productos distintos, valor total, producto más caro
    y producto con mayor stock.
 
    Argumentos:
        inventario (list): Lista de productos existentes
    """
    # Si no hay productos, mostrar mensaje y salir
    if not inventario:
        print("Sin datos")
        return

    total_productos = len(inventario)  # Cantidad de productos distintos
    valor = 0        # Valor total del inventario
    p_caro = inventario[0]    # Inicializar producto más caro
    p_stock = inventario[0]   # Inicializar producto mayor stock

    for p in inventario:
        valor += (p["precio"] * p["cantidad"])     # Sumar valor total
        if p["precio"] > p_caro["precio"]:         # Actualizar más caro
            p_caro = p
        if p["cantidad"] > p_stock["cantidad"]:    # Actualizar mayor stock
            p_stock = p

    # Mostrar estadísticas calculadas
    print(f"Total Productos: {total_productos}")
    print(f"Valor Total: {valor}")
    print(f"Más Caro: {p_caro['nombre']}")
    print(f"Mayor Stock: {p_stock['nombre']}")
