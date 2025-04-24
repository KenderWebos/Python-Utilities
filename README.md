# Utilidades Python

Una colección de utilidades Python para diversas tareas, incluyendo procesamiento de texto, conversión de medios, automatización y más.

## Estructura del Repositorio

El repositorio está organizado en las siguientes categorías principales:

- **text-processing/**: Herramientas de conversión y procesamiento de texto
- **media-generation/**: Utilidades de generación de medios y recursos
- **automation/**: Scripts y herramientas de automatización
- **system-utilities/**: Utilidades a nivel de sistema
- **web-tools/**: Web scraping y utilidades web
- **whatsapp-tools/**: Herramientas de automatización de WhatsApp
- **ui-tools/**: Componentes y frameworks de UI
- **misc/**: Utilidades misceláneas y ejemplos

## Categorías y Utilidades

### Procesamiento de Texto (`text-processing/`)

- **Texto a PDF** (`text-processing/text-to-pdf/`)
  - `text-to-pdf.py`: Aplicación GUI para convertir texto a archivos PDF

- **Texto a Voz** (`text-processing/text-to-speach/`)
  - `text-to-speach-simple.py`: Convertidor simple de texto a voz usando pyttsx3
  - `text-to-speach-mp3.py`: Convierte texto a archivos de audio MP3
  - `dp-text-to-speach.py`: Aplicación avanzada de texto a voz

### Generación de Medios (`media-generation/`)

- **Generador de Códigos QR** (`media-generation/qr-generator/`)
  - `text-to-qr.py`: Genera códigos QR a partir de texto o URLs

- **Generadores de Nombres** (`media-generation/`)
  - `short-name-generator.py`: Genera nombres cortos
  - `short-name-generator-gpt-version.py`: Versión mejorada con GPT del generador de nombres

### Automatización (`automation/`)

- **Auto-GUI** (`automation/auto-gui/`)
  - `clicks.py`: Automatiza clics del mouse
  - `Contestador_de_encuestas.py`: Herramienta automatizada para respuesta de encuestas

- **Proyecto Key Sound** (`automation/key_sound_project/`)
  - `key_sound.py`: Reproduce diferentes sonidos basados en categorías de teclas (letras, números, símbolos, teclas de función)

### Utilidades de WhatsApp (`whatsapp-tools/`)

- **Herramientas de WhatsApp** (`whatsapp-tools/wsp-utilities/`)
  - `wsp-direct.py`: Abre chat directo de WhatsApp con un número específico
  - `wsp-spam-bomb.py`: Herramienta de automatización de mensajes de WhatsApp

### Herramientas Web (`web-tools/`)

- **Web Scraping** (`web-tools/web-scrapping/`)
  - `yapo-ws-webscraping.py`: Utilidad de web scraping para sitios web específicos

### Componentes UI (`ui-tools/`)

- **Herramientas UI para Python** (`ui-tools/ui-for-py/`)
  - `coding.py`: Componentes UI para aplicaciones de codificación
  - `example.py`: Ejemplos de implementaciones UI
  - `main.py`: Framework principal de UI

### Utilidades de Sistema (`system-utilities/`)

- **Herramientas de Sistema** (`system-utilities/utilities/`)
  - Varios scripts y herramientas de utilidades del sistema
  - `open-current-folder.py`: Abre la carpeta actual en el explorador de archivos

### Misceláneos (`misc/`)

- **Herramientas Varias**
  - `a-simple-joke.py`: Muestra chistes
  - Utilidades adicionales en subdirectorios:
    - `api-testing/`: Utilidades para pruebas de API
    - `args-py/`: Procesamiento de argumentos de línea de comandos
    - `calendar-py/`: Herramientas relacionadas con calendario
    - `ChatGPT/`: Herramientas de integración con ChatGPT
    - Y más...

## Instalación

La mayoría de las utilidades requieren Python 3.6 o superior. Cada utilidad puede tener dependencias específicas que pueden instalarse a través de pip.

Dependencias comunes incluyen:
- pyttsx3 (para texto a voz)
- pygame (para aplicaciones de audio)
- qrcode (para generación de códigos QR)
- fpdf (para generación de PDF)
- PyAutoGUI (para herramientas de automatización)

## Uso

Cada utilidad está diseñada para ejecutarse de forma independiente. Navega al directorio específico y ejecuta el script de Python:

```bash
python nombre_del_script.py
```

## Contribuciones

Siéntete libre de contribuir añadiendo nuevas utilidades o mejorando las existentes. Sigue la estructura de código existente y añade la documentación apropiada. 