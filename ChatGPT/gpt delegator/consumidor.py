import os
import pyperclip  # Importa el módulo pyperclip

# Carpeta raíz de tu proyecto
ruta_proyecto = './'

# Función para recopilar el contenido de los archivos de texto y etiquetarlos

def recopilar_contenido(ruta):
    contenido_total = ""
    for carpeta_actual, carpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            # Filtra los tipos de archivos deseados
            if archivo.endswith(('.html', '.css', '.js', '.txt')):
                nombre_archivo = os.path.basename(archivo)
                
                contenido_total += f"--- --- --- --- ---\n"
                contenido_total += f"{nombre_archivo} start\n"
                ruta_completa = os.path.join(carpeta_actual, archivo)
                with open(ruta_completa, 'r', encoding='utf-8') as archivo_actual:
                    contenido_archivo = archivo_actual.read()
                    contenido_total += contenido_archivo
                contenido_total += f"{nombre_archivo} end\n"
                contenido_total += f"--- --- --- --- ---\n"


    return contenido_total

# Llama a la función con la ruta de tu proyecto
contenido_total = recopilar_contenido(ruta_proyecto)

# Guarda el contenido en un archivo o en la estructura que desees
with open('kernel.txt', 'w', encoding='utf-8') as archivo_salida:
    archivo_salida.write(contenido_total)

aux = "a"

with open('kernel.txt', "r", encoding='utf-8') as contenido_archivo:
    aux = contenido_archivo.read()

# Copia el contenido al portapapeles
pyperclip.copy(aux)
