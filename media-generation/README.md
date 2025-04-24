# Utilidades de Generación de Medios

Este directorio contiene utilidades para generar varios tipos de contenido multimedia:

## Generador de Códigos QR

Ubicado en `qr-generator/`

- `text-to-qr.py`: Genera códigos QR a partir de texto o URLs utilizando la biblioteca qrcode

## Generadores de Nombres

Ubicados en el directorio principal:

- `short-name-generator.py`: Genera nombres cortos utilizando algoritmos simples
- `short-name-generator-gpt-version.py`: Versión mejorada que utiliza técnicas similares a GPT para una generación de nombres más natural

## Uso

Cada utilidad está diseñada para ejecutarse de forma independiente. Para usar el generador de QR:

```bash
cd qr-generator
python text-to-qr.py
```

Para los generadores de nombres, ejecuta directamente desde este directorio:

```bash
python short-name-generator.py
# o
python short-name-generator-gpt-version.py
``` 