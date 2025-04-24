from gtts import gTTS

myText = input("Escribe algo para que sea leido \n")

lenguaje="es"
output = gTTS(text=myText, lang=lenguaje, slow=False)
output.save("output.mp3")

import os

os.system("start output.mp3")
os.system("pause")