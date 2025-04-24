import random

# Definir las vocales y consonantes.
bocales = ['a', 'e', 'i', 'o', 'u']
consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

# Patrón CVCVCV (Consonante-Vocal-Consonante-Vocal-Consonante-Vocal)
# Este patrón es más natural y fluido, ya que muchas palabras en diversos idiomas siguen una estructura alterna de consonantes y vocales.
for i in range(10):  # Número de filas de nombres generados.
    for j in range(10):  # Número de nombres por fila.
        name = ""
        
        # Generamos una secuencia alternando consonantes y vocales:
        name += random.choice(consonantes)  # C (Consonante)
        name += random.choice(bocales)  # V (Vocal)
        name += random.choice(consonantes)  # C (Consonante)
        name += random.choice(bocales)  # V (Vocal)
        name += random.choice(consonantes)  # C (Consonante)
        name += random.choice(bocales)  # V (Vocal)
        
        print(name, end=" ")  # Imprimir el nombre generado en una línea.
    print()  # Salto de línea al final de cada fila.

# Posibles mejoras para mejorar la naturalidad de las palabras generadas:

# 1. Variabilidad en las combinaciones:
#    - Alterna entre diferentes patrones de generación. Por ejemplo, en lugar de CVCVCV, puedes probar otros como CVCCVC.
#    - Introduce variabilidad en las combinaciones de letras, por ejemplo, usando consonantes más suaves o más duras para generar diferentes tipos de sonidos.

# 2. Evitar secuencias difíciles:
#    - Algunas combinaciones como "qq", "zz", "xx" son poco comunes en muchos idiomas y pueden sonar extrañas. 
#    - Puedes filtrar estas combinaciones para que no se generen. 

# 3. Incluir reglas fonéticas específicas:
#    - Si buscas palabras que suenen mejor en un idioma específico, puedes adaptar las combinaciones a las reglas fonéticas de ese idioma.
#    - Por ejemplo, en español, ciertas combinaciones como "ch" o "ll" son comunes, mientras que en inglés pueden aparecer combinaciones como "sh" o "th".
#    - Considera usar listas predefinidas de combinaciones de consonantes y vocales que se ajusten mejor al idioma de destino.

# 4. Añadir prefijos o sufijos comunes:
#    - Si deseas generar nombres o palabras que suenen más familiares, puedes agregar prefijos o sufijos comunes en el idioma elegido.
#    - Por ejemplo, en inglés podrías añadir "-ly" al final de algunas palabras para hacerlas adjetivos, o "-er" para hacerlas sustantivos (como "runner").

# 5. Ajustar el número de sílabas:
#    - Si prefieres que las palabras generadas tengan más o menos sílabas, puedes ajustar el número de consonantes y vocales en el patrón. Por ejemplo, CVCVC es una palabra más corta que CVCVCVC.
