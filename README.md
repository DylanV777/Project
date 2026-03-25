# Project

# Sistema de Gestión de Inventario - Semana 3

Este es un proyecto de consola desarrollado en Python para la gestión de productos, precios y stock. Permite realizar operaciones CRUD, calcular estadísticas y persistir datos en archivos CSV.

## 🚀 Funcionalidades
*   **Gestión de Productos:** Agregar, buscar, actualizar y eliminar.
*   **Validación Robusta:** Control de errores en entradas numéricas y prevención de valores negativos.
*   **Estadísticas:** Cálculo de unidades totales, valor del inventario, producto más caro y mayor stock.
*   **Persistencia:** Guardado y carga de datos mediante archivos CSV con manejo de excepciones.
*   **Seguridad de Salida:** Avisa si hay cambios sin guardar antes de cerrar el programa.

## 📂 Estructura del Proyecto
*   `app.py`: Interfaz de usuario y menú principal.
*   `servicios.py`: Lógica de negocio y manipulación del inventario.
*   `archivos.py`: Manejo de lectura y escritura de archivos CSV.
*   `inventario.csv`: Archivo de datos (se genera automáticamente).

## 🛠️ Instalación y Uso
1. Clona el repositorio o descarga los archivos.
2. Asegúrate de tener Python 3 instalado.
3. Ejecuta el programa principal:
   ```bash
   python app.py
