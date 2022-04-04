import time
import os
from tkinter import *
from datetime import datetime

def startLink(num):
    os.system( str("start " + links[num][1]) )

root = Tk()
root.title("Iniciar Clase")
root.geometry("300x400")

links = [

    #Ingles
    ["Ingles_martes", "https://uvirtual2.ucsc.cl/mod/zoom/view.php?id=2445367"],
    ["Ingles_jueves", "https://uvirtual2.ucsc.cl/mod/zoom/view.php?id=2446625"],
    #Probabilidad y estadistica
    ["Probabilidad_catedra", "https://uvirtual2.ucsc.cl/mod/zoom/view.php?id=2458313"],
    ["Probabilidad_ayudantia", "https://uvirtual2.ucsc.cl/mod/zoom/view.php?id=2459718"],
    ["Probabilidad_laboratorio", "https://uvirtual2.ucsc.cl/mod/zoom/view.php?id=2459804"],
    #Electromagnetismo y circuitos
    ["Electromagnetismo_catedra", "https://uvirtual2.ucsc.cl/mod/zoom/view.php?id=2459338"],
    ["Electromagnetismo_ayudantia", "https://uvirtual2.ucsc.cl/mod/zoom/view.php?id=2462135"],
    #Teoria de sistemas
    ["TeoriaDeSistemas", "none"],
    #Bases de datos
    ["BasesDeDatos_catedra", "https://uvirtual2.ucsc.cl/mod/zoom/view.php?id=2457180"],
    ["BasesDeDatos_laboratorio", "https://uvirtual2.ucsc.cl/mod/zoom/view.php?id=2447585"],
    #EVA
    ["EVA", "https://uvirtual2.ucsc.cl/my/"],
    #Typing
    ["Typing_1", "https://www.typingclub.com/sportal/program-3/217.play"],
    ["Typing_2", "https://10fastfingers.com/typing-test/spanish"],

]

#for i in range (10):
    
btn1 = Button(root, text= links[0][0] , command = lambda:startLink(0) )
btn1.pack()
btn1 = Button(root, text= links[1][0] , command = lambda:startLink(1) )
btn1.pack()
btn1 = Button(root, text= links[2][0] , command = lambda:startLink(2) )
btn1.pack()
btn1 = Button(root, text= links[3][0] , command = lambda:startLink(3) )
btn1.pack()
btn1 = Button(root, text= links[4][0] , command = lambda:startLink(4) )
btn1.pack()
btn1 = Button(root, text= links[5][0] , command = lambda:startLink(5) )
btn1.pack()
btn1 = Button(root, text= links[6][0] , command = lambda:startLink(6) )
btn1.pack()
btn1 = Button(root, text= links[7][0] , command = lambda:startLink(7) )
btn1.pack()
btn1 = Button(root, text= links[8][0] , command = lambda:startLink(8) )
btn1.pack()
btn1 = Button(root, text= links[9][0] , command = lambda:startLink(9) )
btn1.pack()
btn1 = Button(root, text= links[10][0] , command = lambda:startLink(10) )
btn1.pack()

btn1 = Button(root, text= links[11][0] , command = lambda:startLink(11) )
btn1.pack()
btn1 = Button(root, text= links[12][0] , command = lambda:startLink(12) )
btn1.pack()

root.mainloop()