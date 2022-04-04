from gtts import gTTS
import os
import time
import pyautogui
from pygame import mixer

myText = input("Escribe algo para que sea leido \n")

lenguaje="es" #es en
output = gTTS(text=myText, lang=lenguaje, slow=False)
output.save("output.mp3")

os.system("start output.mp3")