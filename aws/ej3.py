def solicitar_datos_personales():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    hobby = input("¿Cuál es tu hobby favorito? ")
    
    print("\n--- Datos para calcular tu IMC (Índice de Masa Corporal) ---")
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros (ej. 1.75): "))
    
    imc = peso / (altura ** 2)
    
    print("\n--- Tus datos personales ---")
    print(f"Nombre completo: {nombre} {apellido}")
    print(f"Edad: {edad} años")
    print(f"Hobby: {hobby}")
    print("\n--- Resultado IMC ---")
    print(f"Tu IMC es: {imc:.2f}")
    
    if imc < 18.5:
        print("Clasificación: Bajo peso")
    elif 18.5 <= imc < 25:
        print("Clasificación: Peso normal")
    elif 25 <= imc < 30:
        print("Clasificación: Sobrepeso")
    else:
        print("Clasificación: Obesidad")

solicitar_datos_personales()