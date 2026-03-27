# Importa el módulo para trabajar con archivos CSV
import csv
 
# Función para guardar el inventario en un archivo CSV
 
 
def guardar_csv(inventario):
    """
    Pide la ruta al usuario y guarda el inventario en un archivo CSV.
 
    Argumentos:
        inventario (list): Lista de productos a guardar
    """
    # Pedir la ruta al usuario
    ruta = input("Ingrese el nombre del archivo CSV a guardar: ")
    # Si el inventario está vacío, mostrar mensaje y salir
    if not inventario:
        print("Nada que guardar")
        return
    try:
        # Abrir el archivo en modo escritura
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            # Crear un escritor de diccionarios indicando las columnas
            writer = csv.DictWriter(
                f, fieldnames=["nombre", "precio", "cantidad"])
            writer.writeheader()     # Escribir la cabecera en el CSV
            # Escribir todas las filas del inventario
            writer.writerows(inventario)
        print("Guardado")
    except FileNotFoundError:
        print("Error al guardar")
    except PermissionError:
        print("No tienes permisos")
 
# Función para cargar un inventario desde un archivo CSV
 
 
def cargar_csv():
    """
    Pide la ruta al usuario y carga productos desde un archivo CSV.
    Las filas con datos inválidos son ignoradas automáticamente.
 
    Retorna:
        list: Lista de productos cargados
    """
    # Pedir la ruta al usuario
    ruta = input("Ingrese el nombre del archivo CSV a cargar: ")
    if not ruta.lower().endswith(".csv"):
        print("Solo se permiten archivos CSV")
        return []
    productos = []
    try:
        # Abrir el archivo en modo lectura
        with open(ruta, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            # Recorrer cada fila del CSV
            for fila in reader:
                try:
                    # Extraer y convertir los valores
                    nombre = fila["nombre"]
                    precio = float(fila["precio"])
                    cantidad = int(fila["cantidad"])
                    # Agregar producto a la lista local
                    productos.append(
                        {"nombre": nombre, "precio": precio, "cantidad": cantidad})
                except ValueError:
                    continue
        print("Cargado")
    except FileNotFoundError:
        print("No se encontró el archivo")
    except PermissionError:
        print("No tienes permisos")
    return productos