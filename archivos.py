import csv

def guardar_csv(inventario, ruta):
    if not inventario:
        print("Nada que guardar")
        return
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["nombre", "precio", "cantidad"])
            writer.writeheader()
            writer.writerows(inventario)
        print("Guardado")
    except:
        print("Error al guardar")

def cargar_csv(inventario, ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            # Para cumplir con la política de fusión/sobrescritura sin usar returns
            for fila in reader:
                try:
                    nombre = fila["nombre"]
                    precio = float(fila["precio"])
                    cantidad = int(fila["cantidad"])
                    # Aquí podrías elegir: siempre agregar o buscar y sumar
                    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
                except:
                    continue
        print("Cargado")
    except:
        print("No se encontró el archivo")
