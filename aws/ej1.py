from abc import ABC, abstractmethod
 
# Interface para las operaciones  de la calculadora
class Operacion(ABC):
    @abstractmethod
    def execute(a,b):
        pass
#Clase Calculadora
class Calculadora:
    
    def __init__(self) -> None:
        self.operaciones = {}
    
    def add_operacion(self, name: str ,operation: Operacion):
        self.operaciones[name] = operation
        
    def calcular(self, nombre_operacion,a,b):
        if nombre_operacion not in self.operaciones:
            raise ValueError(f"La operación {nombre_operacion} no está registrada.")
        return self.operaciones[nombre_operacion].execute(a, b)
        
#Operaciones basicas de la calculadora
class Suma(Operacion):
    def execute(self, a, b):
        return a + b
 
class Resta(Operacion):
    def execute(self, a, b):
        return a - b
 
class Multiplicacion(Operacion):
    def execute(self, a, b):
        return a * b
 
class Division(Operacion):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        return a / b
 
# Funcion que muestra el menu principal
def mostrar_menu():
    print("\n--- MENU DE OPERACIONES ---")
    print("1. Añadir Operación")
    print("2. Operar con las operaciones añadidas")
    print("0. Salir")
 
#Funcion que muestra el menu para añadir operaciones
def mostrar_menu_añadir():
    print("Ingresa la operación que deseas añadir")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("'volver'. Volver al menú principal")
 
 
def main():
    #Se crea el objeto calculadora
    calculadora = Calculadora()
    
    print("Bienvenido a la calculadora")
    print("Esta es una calculadora que soporta hasta 4 operaciones basicas con dos números, sin embargo debes añadirlas a la calculadora, por defecto no tiene ninguna")
    
    mostrar_menu()
    opcion_menu_principal = ""
    
    while (opcion_menu_principal != "0"):
        opcion_menu_principal = input()
        
        # Menupara añadir una operación a una calculadora
        if opcion_menu_principal == "1":
            mostrar_menu_añadir()
            operacion_para_añadir = ""
            
            while(operacion_para_añadir != "volver"):
                operacion_para_añadir = input()
                if operacion_para_añadir == "1":
                    print("Has elegido Suma, ingresa un alias para la operacion")
                    calculadora.add_operacion(name=input(), operation=Suma())
                elif operacion_para_añadir == "2":
                    print("Has elegido Resta, ingresa un alias para la operacion")
                    calculadora.add_operacion(name=input(), operation=Resta())
                elif operacion_para_añadir == "3":
                    print("Has elegido Multiplicacion, ingresa un alias para la operacion")
                    calculadora.add_operacion(name=input(), operation=Multiplicacion())
                elif operacion_para_añadir == "4":
                    print("Has elegido Division, ingresa un alias para la operacion")
                    calculadora.add_operacion(name=input(), operation=Division())
                    
                elif operacion_para_añadir == "volver":
                    print("Volviendo al menu principal...")
                    mostrar_menu()
                    break
                else:
                    print("Operación no válida. Intenta de nuevo.")
                    mostrar_menu_añadir()
                    continue
                print("Volviendo al menu principal...")
                mostrar_menu()
                break
            
            continue
        
        elif opcion_menu_principal == "2":
            print("Ingresa la operación que deseas realizar junto a los dos numeros")
            operacion = ""
            while(operacion != "volver"):
                operacion = input()
                partes = operacion.split()
                if(operacion == "volver"):
                    print("Volviendo al menu principal...")
                    mostrar_menu()
                    break
                
                if len(partes) != 3:
                    print("Formato incorrecto. Debe ser: <operacion registrada> <numero1> <numero2>")
                else:
                    nombre_operacion = partes[0]
                    try:
                        a = float(partes[1])
                        b = float(partes[2])
                    except ValueError:
                        print("Los números deben ser válidos.")
                    
                    try:
                        resultado = calculadora.calcular(nombre_operacion, a, b)
                        print(f"Resultado: {resultado}")
                    except ValueError:
                        print("Operación no registrada, ingrese nuevamente o registre una operación o escriba 'volver'")
                    
                
    print("Saliendo de la calculadora...")
    
 
#Inicio del programa
main()