import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

def addApp():
    print("holaMundo")

root.title("Grand Theft Auto 5")
root.resizable()
#structure
canvas = tk.Canvas(root, width=800, height=600, bg="black")
canvas.pack()
frame = tk.Frame(root, bg="blue")
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

#boton
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="black")
openFile.pack()
#boton
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="black", command=addApp)
runApps.pack()

#mainLoop
root.mainloop()
