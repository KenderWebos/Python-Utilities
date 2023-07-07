from gtts import gTTS
import os

myText = input("Escribe algo para que sea leido \n")

lenguaje="es"
output = gTTS(text=myText, lang=lenguaje, slow=False)
output.save("output.mp3")

os.system("start output.mp3")
os.system("pause")