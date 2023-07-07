import pyttsx3
import os

# Crear una instancia de la librería
engine = pyttsx3.init()

def speak():
    # Pedir al usuario que ingrese un texto
    texto = input("Ingresa un texto para leer en voz alta: ")

    # Establecer el idioma en español
    engine.setProperty('voice', 'spanish')

    # Leer el texto en voz alta
    engine.say(texto)
    engine.runAndWait()

while(True):
    speak()

# os.system("pause")