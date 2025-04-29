import tkinter as tk
from tkinter import simpledialog, messagebox

def agregar_tarea():
    tarea = simpledialog.askstring("Agregar", "Nueva tarea:")
    if tarea and tarea.strip():  # Verifica que no esté vacío
        lista_tareas.insert(tk.END, tarea)
        guardar_tareas()
    elif tarea:  # Si solo contiene espacios
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía")

def editar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        tarea_actual = lista_tareas.get(seleccion)
        # Elimina el checkmark si existe para editar
        tarea_limpia = tarea_actual[2:] if tarea_actual.startswith("✓ ") else tarea_actual
        nueva_tarea = simpledialog.askstring("Editar", "Editar tarea:", initialvalue=tarea_limpia)
        if nueva_tarea and nueva_tarea.strip():
            lista_tareas.delete(seleccion)
            # Mantiene el estado de completado
            if tarea_actual.startswith("✓ "):
                lista_tareas.insert(seleccion, f"✓ {nueva_tarea}")
            else:
                lista_tareas.insert(seleccion, nueva_tarea)
            guardar_tareas()
        elif nueva_tarea:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía")

def marcar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        tarea = lista_tareas.get(seleccion)
        if tarea.startswith("✓ "):
            lista_tareas.delete(seleccion)
            lista_tareas.insert(seleccion, tarea[2:])  # Quita el checkmark
        else:
            lista_tareas.delete(seleccion)
            lista_tareas.insert(seleccion, f"✓ {tarea}")  # Agrega checkmark
        guardar_tareas()

def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        respuesta = messagebox.askyesno("Confirmar", "¿Eliminar esta tarea?")
        if respuesta:
            lista_tareas.delete(seleccion)
            guardar_tareas()

def guardar_tareas():
    with open("tareas.txt", "w") as f:
        tareas = lista_tareas.get(0, tk.END)
        for tarea in tareas:
            f.write(tarea + "\n")

def cargar_tareas():
    try:
        with open("tareas.txt", "r") as f:
            for linea in f:
                lista_tareas.insert(tk.END, linea.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("Lista de Tareas")

# Configuración de colores
root.configure(bg="#f0f0f0")
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

lista_tareas = tk.Listbox(
    frame, 
    width=50, 
    height=10, 
    font=('Arial', 12),
    selectbackground="#a6a6a6",
    selectforeground="white"
)
lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

lista_tareas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_tareas.yview)

# Frame para botones
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=5)

btn_agregar = tk.Button(
    btn_frame, 
    text="Agregar", 
    command=agregar_tarea,
    bg="#4CAF50",
    fg="white",
    width=10
)
btn_editar = tk.Button(
    btn_frame, 
    text="Editar", 
    command=editar_tarea,
    bg="#2196F3",
    fg="white",
    width=10
)
btn_marcar = tk.Button(
    btn_frame, 
    text="Marcar/Desmarcar", 
    command=marcar_tarea,
    bg="#FF9800",
    fg="white",
    width=15
)
btn_eliminar = tk.Button(
    btn_frame, 
    text="Eliminar", 
    command=eliminar_tarea,
    bg="#f44336",
    fg="white",
    width=10
)

btn_agregar.pack(side=tk.LEFT, padx=5)
btn_editar.pack(side=tk.LEFT, padx=5)
btn_marcar.pack(side=tk.LEFT, padx=5)
btn_eliminar.pack(side=tk.LEFT, padx=5)

# Cargar tareas al iniciar
cargar_tareas()

root.mainloop()