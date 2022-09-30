#objetivo poder guardar textos segun una fecha que se entrega por consola con el fomato "dia mes año texto"
#desarrolladores: Kevin Campos
#calendarProject®

import time
import os
import sys
import json
import kender
#import consoleManager

#variables
db = []

def add():
    print("Añadiendo al calendario:")
    while(True):
        mainText = input("> ")

        if(mainText != "0"):
            db.append(mainText)
        else:
            break
    pass

def show():
    print("")
    print(db)
    print("")
    pass

def exit():
    os.system("cls")
    print("> Saliendo del programa")
    time.sleep(0.5)
    os.system("cls")
    print("> Saliendo del programa.")
    time.sleep(0.5)
    os.system("cls")
    print("> Saliendo del programa..")
    time.sleep(0.5)
    os.system("cls")
    print("> Saliendo del programa...")
    time.sleep(0.5)
    os.system("cls")
    sys.exit()

def help():
    print("add -> Añadir una entrada al calendario")
    print("show -> Mostrar el calendario")
    print("exit -> Salir del programa")
    print("help -> Mostrar este mensaje")

def getArgs(args):

    kender.makeSpace(7)

    if args == "add":
        add( )
    if args == "show":
        show( )
    if args == "exit":
        exit( )
    if args == "help":
        help( )   

    kender.makeSpace(7)

# le falta muchas mejoras args debe ser el array de argumentos y manejar los errores

def main():
    kender.alert("Bienvenido al calendario")
    while True:
        getArgs(input("> "))

main()