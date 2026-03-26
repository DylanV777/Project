# Importa el módulo para trabajar con archivos CSV
import csv

# Función para guardar el inventario en un archivo CSV


def guardar_csv(inventario, ruta):
    """
    Guarda el inventario en un archivo CSV.
 
    Argumentos:
        inventario (list): Lista de productos a guardar
        ruta (str): Ruta del archivo CSV de destino
    """
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


def cargar_csv(inventario, ruta):
    """
    Carga productos desde un archivo CSV al inventario.
    Las filas con datos inválidos son ignoradas automáticamente.
 
    Argumentos:
        inventario (list): Lista donde se cargarán los productos
        ruta (str): Ruta del archivo CSV a leer
    """
    if not ruta.lower().endswith(".csv"):
        print("Solo se permiten archivos CSV")
        return
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
                    # Agregar producto al inventario
                    inventario.append(
                        {"nombre": nombre, "precio": precio, "cantidad": cantidad})
                except ValueError:
                    continue
        print("Cargado")
    except FileNotFoundError:
        print("No se encontró el archivo")
    except PermissionError:
        print("No tienes permisos")
