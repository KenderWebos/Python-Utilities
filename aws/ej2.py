def analizar_frase():
    # Solicitar frase al usuario
    frase = input("Ingrese una frase: ").lower()
    
    # Contar caracteres totales (sin espacios)
    frase_sin_espacios = frase.replace(" ", "")
    total_caracteres = len(frase_sin_espacios)
    
    # Contar vocales y consonantes
    vocales = 0
    consonantes = 0
    vocales_lista = {'a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú'}
    
    for caracter in frase_sin_espacios:
        if caracter in vocales_lista:
            vocales += 1
        elif caracter.isalpha():  # Verifica si es letra
            consonantes += 1
    
    # Verificar palíndromo (ignorando espacios y mayúsculas)
    es_palindromo = frase_sin_espacios == frase_sin_espacios[::-1]
    
    # Mostrar resultados
    print("\nResultados del análisis:")
    print(f"- Total de caracteres: {total_caracteres}")
    print(f"- Vocales: {vocales}")
    print(f"- Consonantes: {consonantes}")
    print(f"- Es palíndromo: {'Sí' if es_palindromo else 'No'}")
    
    
# Ejecutar la función
if __name__ == "__main__":
    analizar_frase()