import tkinter
import os

def enviar():
    value = text1.get("1.0","end-1c") #(1.0, "end")
    print(value)
    value = value.replace(" ","+")
    os.system("start https://www.youtube.com/results?search_query="+value)

root = tkinter.Tk()
root.title("Youtube search manager")
text1 = tkinter.Text(root, width=80, height=1)
button1 = tkinter.Button(root, text="Enviar", width=8, height=2, command = enviar)

root.geometry("+640+500")

text1.pack()
button1.pack()
root.mainloop()