from pyautogui import *
import pyautogui
import time
import keyboard
import random
import os

clickTime = 0.25
numberSelected = 0

print("> Este es un producto informatico orientado a la automatizacion, \ncualquier uso indevido en aplicaciones de terceros es de mera responsabilidad de el usuario.")
print("> Autor: KenerCorp inc")
print("> Licencia: libre de derechos")
print("> Version: 1.0")
print("\n")

def clickOn(interX, interY):
    pyautogui.mouseDown(x = interX, y= interY)
    pyautogui.mouseUp(x = interX, y= interY)

def VolverAJugar():
    #modulo 1
    varX = 1225
    varY = 318
    clickOn(varX, varY)
    time.sleep(clickTime)

    #modulo 2
    varX = 1213
    varY = 664
    clickOn(varX, varY)
    
    pyautogui.mouseUp()
    time.sleep(clickTime)

def AceptarPartida():
    #modulo 1
    varX = 1049
    varY = 278
    clickOn(varX, varY)
    time.sleep(clickTime)

    #modulo 2
    varX = 1049
    varY = 619
    clickOn(varX, varY)
    time.sleep(clickTime)

def Rendirse():
    #Rendirse

    #1
    pyautogui.click(x = 1252, y=10)
    time.sleep(clickTime)

    pyautogui.mouseDown(x = 900, y=212) #pantalla
    pyautogui.mouseUp(x = 900, y=212)
    time.sleep(clickTime)

    pyautogui.mouseDown(x = 1231, y=74) #Boton
    pyautogui.mouseUp(x = 1231, y=74)
    time.sleep(clickTime)
    pyautogui.mouseDown(x = 1103, y=242) #Rendirse
    pyautogui.mouseUp(x = 1103, y=242)
    time.sleep(clickTime)

    #2
    pyautogui.mouseDown(x = 900, y=550) #pantalla
    pyautogui.mouseUp(x = 900, y=550)
    
    pyautogui.mouseDown(x = 1231, y=410) #Boton
    pyautogui.mouseUp(x = 1231, y=410)
    time.sleep(clickTime)
    pyautogui.mouseDown(x = 1119, y=577) #Rendirse
    pyautogui.mouseUp(x = 1119, y=577)
    time.sleep(clickTime)

    pyautogui.mouseUp()
    time.sleep(clickTime)

#pyautogui.displayMousePosition()

while(1):
    numberSelected = 0
    if(numberSelected == 0):
        
        a = 1
        while(a == 1):

            if pyautogui.locateOnScreen("aceptar.png", confidence = 0.5) != None:
                print("i can see the START btn")

                AceptarPartida()
                a = 0
                print("> match started <")
            else:
                print("i cant see START btn")
                time.sleep(1)

        print("- Inicializando cronometro -")
        time.sleep(60)
        print("- First minute -")
        time.sleep(60*4)
        print("- 4 minutes remaining -")
        time.sleep(60*4)
        print("- Scanning... -")

        a = 1
        while(a == 1):

            if pyautogui.locateOnScreen("tuerca.png", confidence = 0.9) != None:
                print("i can see it")
                Rendirse()

                time.sleep(20)

                VolverAJugar()
                a = 0
            else:
                print("i cant see nothing")
                time.sleep(5)
       
    os.system("cls")

"""
Esto es un comentario
"""