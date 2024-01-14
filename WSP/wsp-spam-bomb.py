import pyautogui
import time
import os


def spamMachine():
    time.sleep(8)
    pyautogui.press("enter")

    for i in range(50):
        pyautogui.write( "perdon sebita yo no queria" )
        pyautogui.press("enter")
        
        pass
    pyautogui.alert('Bomba de mensajes finalizada')


number = input("(bomba de mensajes en SPAM) \n ingrese el numero \n +569")

print(number)
os.system("start https://web.whatsapp.com/send?phone=569"+ number +"&text=hola")

spamMachine()

