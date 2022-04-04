import os

#phone_no = "+56935732428"

phone_no = input("Escribe un numero en el formato +56950376005 \n")

parsedMessage = "hola"

url = 'https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage

os.system("start " + url)