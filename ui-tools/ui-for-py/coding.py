import tkinter as tk
from tkinter import messagebox, filedialog

def show_messagebox():
    messagebox.showinfo("Mensaje", "¡Esto es un cuadro de diálogo!")

def open_file():
    file = filedialog.askopenfilename()
    print("Archivo seleccionado:", file)

root = tk.Tk()
root.title("Panel de muestra de Tkinter")
root.geometry("400x300")

# Estilos
bg_color = "#f1f1f1"
button_color = "#4c72b0"
button_text_color = "white"
entry_bg_color = "#e4e4e4"
entry_text_color = "black"

# Configuración global de estilo
root.configure(bg=bg_color)

# Etiqueta
label = tk.Label(root, text="Etiqueta", bg=bg_color, fg="black", font=("Arial", 12))
label.pack(pady=10)

# Botón
button = tk.Button(root, text="Botón", bg=button_color, fg=button_text_color, font=("Arial", 12))
button.pack(pady=5)

# Cuadro de entrada
entry = tk.Entry(root, bg=entry_bg_color, fg=entry_text_color, font=("Arial", 12))
entry.pack(pady=5)

# Cuadro de texto
text = tk.Text(root, bg=entry_bg_color, fg=entry_text_color, font=("Arial", 12), height=5)
text.pack(pady=5)

# Cuadro de lista
listbox = tk.Listbox(root, bg=entry_bg_color, fg=entry_text_color, font=("Arial", 12))
listbox.pack(pady=5)
listbox.insert(tk.END, "Elemento 1")
listbox.insert(tk.END, "Elemento 2")
listbox.insert(tk.END, "Elemento 3")

# Cuadro de verificación
check_var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Casilla de verificación", variable=check_var, bg=bg_color, fg="black", font=("Arial", 12))
checkbox.pack(pady=5)

# Menú desplegable
options = ["Opción 1", "Opción 2", "Opción 3"]
selected_option = tk.StringVar()
selected_option.set(options[0])
dropdown = tk.OptionMenu(root, selected_option, *options)
dropdown.config(bg=entry_bg_color, fg=entry_text_color, font=("Arial", 12))
dropdown.pack(pady=5)

# Cuadro de diálogo
messagebox_button = tk.Button(root, text="Cuadro de diálogo", bg=button_color, fg=button_text_color, font=("Arial", 12), command=show_messagebox)
messagebox_button.pack(pady=5)

# Selector de archivo
file_button = tk.Button(root, text="Seleccionar archivo", bg=button_color, fg=button_text_color, font=("Arial", 12), command=open_file)
file_button.pack(pady=5)

root.mainloop()
