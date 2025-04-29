def dibujar_rombo(n):
    total_asteriscos = 0
    for i in range(1, n + 1):
        espacios = ' ' * (n - i)
        asteriscos = '* ' * i
        print(espacios + asteriscos)
        total_asteriscos += i
    
    for i in range(n - 1, 0, -1):
        espacios = ' ' * (n - i)
        asteriscos = '* ' * i
        print(espacios + asteriscos)
        total_asteriscos += i
    
    return total_asteriscos

try:
    tamaño = int(input("Ingrese el tamaño del rombo (número entero positivo): "))
    if tamaño > 0:
        asteriscos_totales = dibujar_rombo(tamaño)
        print(f"\nEl rombo está compuesto por {asteriscos_totales} asteriscos en total.")
    else:
        print("Por favor ingrese un número positivo.")
except ValueError:
    print("Por favor ingrese un número entero válido.")