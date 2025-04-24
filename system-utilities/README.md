# Utilidades del Sistema

Este directorio contiene scripts y herramientas para interactuar con el sistema operativo y realizar tareas a nivel de sistema.

## Herramientas de Sistema

Ubicado en `utilities/`

- Scripts para tareas comunes del sistema
- `open-current-folder.py`: Abre la carpeta actual en el explorador de archivos

## Otras Utilidades

- Herramientas para la gestión del sistema operativo
- Scripts de configuración y mantenimiento

## Dependencias

Estas utilidades generalmente utilizan:
- Bibliotecas estándar de Python (os, sys, subprocess)
- Módulos específicos del sistema operativo (cuando sea necesario)

## Uso

Para abrir la carpeta actual en el explorador:

```bash
python open-current-folder.py
```

## Compatibilidad

Algunos scripts pueden ser específicos para ciertos sistemas operativos:
- Windows: scripts .bat y .ps1
- Linux/Unix: scripts .sh
- Multiplataforma: scripts .py

Verifica los comentarios dentro de cada script para conocer requisitos específicos de compatibilidad. 