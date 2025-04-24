# Ruta del archivo "all-content.txt"
archivo_contenido = "all-content.txt"

# Ruta de la carpeta "x"
carpeta_src = "SRC"

# Crear la carpeta "x" si no existe
import os
if not os.path.exists(carpeta_src):
    os.makedirs(carpeta_src)

# Leer el contenido desde el archivo "all-content.txt"
with open(archivo_contenido, "r") as contenido_archivo:
    contenido_total = contenido_archivo.read()

# Separar el contenido por secciones
secciones = contenido_total.split("contenido_total.txt end")

# Crear archivos en la carpeta "x"
for i, seccion in enumerate(secciones):
    if seccion.strip():  # Ignorar secciones vacías
        nombre_archivo = os.path.join(carpeta_src, f"archivo_{i}.html")
        with open(nombre_archivo, "w") as archivo:
            archivo.write(seccion)

print(f"Se han creado {len(secciones)} archivos en la carpeta 'x'.")
