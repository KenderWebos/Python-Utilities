import os
from tkinter import *

links = [
    # EVA
    ["EVA", "https://uvirtual2.ucsc.cl/my/"],
    # Typing
    ["Typing 1", "https://www.typingclub.com/sportal/program-3/217.play"],
    ["Typing 2", "https://10fastfingers.com/typing-test/spanish"],
    ["Facebook", "https://www.facebook.com/marketplace/?ref=app_tab"]
]

def startLink(num):
    os.system(str("start " + links[num][1]))

root = Tk()
root.title("kDirectLink")
root.geometry("300x400")

row = 0
column = 0

for link in links:
    btn = Button(root, text=link[0], command=lambda num=links.index(link): startLink(num))
    btn.grid(row=row, column=column, pady=5)
    column += 1

    # Ajustar las columnas a medida que se llena la fila
    if column == 3:
        column = 0
        row += 1

root.mainloop()
