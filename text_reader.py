import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import pyttsx3
import os

class TextReader:
    def __init__(self, root):
        self.root = root
        self.root.title("Lector de Texto Avanzado")
        self.root.geometry("800x600")
        
        # Configuración del motor de texto a voz
        self.engine = pyttsx3.init()
        
        # Configuración de la interfaz
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Área de texto con scroll
        self.text_area = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=80, height=20)
        self.text_area.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Frame para los controles
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=5)
        
        # Botones de control
        button_frame = ttk.Frame(control_frame)
        button_frame.pack(side=tk.LEFT, padx=5)
        
        read_button = ttk.Button(button_frame, text="Leer Texto", command=self.read_text)
        read_button.pack(side=tk.LEFT, padx=5)
        
        stop_button = ttk.Button(button_frame, text="Detener", command=self.stop_reading)
        stop_button.pack(side=tk.LEFT, padx=5)
        
        # Botones de archivo
        file_frame = ttk.Frame(control_frame)
        file_frame.pack(side=tk.LEFT, padx=5)
        
        save_button = ttk.Button(file_frame, text="Guardar", command=self.save_text)
        save_button.pack(side=tk.LEFT, padx=5)
        
        load_button = ttk.Button(file_frame, text="Abrir", command=self.load_text)
        load_button.pack(side=tk.LEFT, padx=5)
        
        # Configuración de voz
        voice_frame = ttk.LabelFrame(control_frame, text="Voz")
        voice_frame.pack(side=tk.LEFT, padx=10)
        
        self.voice_var = tk.StringVar()
        voices = self.engine.getProperty('voices')
        voice_names = [voice.name for voice in voices]
        
        voice_combo = ttk.Combobox(voice_frame, textvariable=self.voice_var, values=voice_names)
        voice_combo.pack(padx=5, pady=5)
        if voice_names:
            voice_combo.set(voice_names[0])
            self.engine.setProperty('voice', voices[0].id)
        
        # Configuración de velocidad
        speed_frame = ttk.LabelFrame(control_frame, text="Velocidad")
        speed_frame.pack(side=tk.LEFT, padx=10)
        
        self.speed_var = tk.StringVar(value="normal")
        speeds = [("Lenta", "slow"), ("Normal", "normal"), ("Rápida", "fast")]
        
        for text, value in speeds:
            ttk.Radiobutton(speed_frame, text=text, variable=self.speed_var,
                          value=value, command=self.update_speed).pack(side=tk.LEFT, padx=5)
        
        # Configuración de volumen
        volume_frame = ttk.LabelFrame(control_frame, text="Volumen")
        volume_frame.pack(side=tk.LEFT, padx=10)
        
        self.volume_var = tk.DoubleVar(value=1.0)
        volume_scale = ttk.Scale(volume_frame, from_=0.0, to=1.0, variable=self.volume_var,
                               command=self.update_volume, orient=tk.HORIZONTAL)
        volume_scale.pack(padx=5, pady=5)
        
        # Atajos de teclado
        self.root.bind('<Control-s>', lambda e: self.save_text())
        self.root.bind('<Control-o>', lambda e: self.load_text())
        self.root.bind('<Control-r>', lambda e: self.read_text())
        self.root.bind('<Escape>', lambda e: self.stop_reading())
    
    def read_text(self):
        text = self.text_area.get("1.0", tk.END)
        if text.strip():
            self.engine.say(text)
            self.engine.runAndWait()
    
    def stop_reading(self):
        self.engine.stop()
    
    def update_speed(self):
        speed = self.speed_var.get()
        if speed == "slow":
            self.engine.setProperty('rate', 100)
        elif speed == "normal":
            self.engine.setProperty('rate', 200)
        elif speed == "fast":
            self.engine.setProperty('rate', 300)
    
    def update_volume(self, value):
        self.engine.setProperty('volume', float(value))
    
    def save_text(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(self.text_area.get("1.0", tk.END))
                messagebox.showinfo("Éxito", "Archivo guardado correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {str(e)}")
    
    def load_text(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    self.text_area.delete("1.0", tk.END)
                    self.text_area.insert("1.0", file.read())
                messagebox.showinfo("Éxito", "Archivo cargado correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextReader(root)
    root.mainloop() 