import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from gtts import gTTS
import os

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Texto a MP3")
        self.root.geometry("600x500")
        
        # Configuración inicial
        self.idiomas = [
            ('Español', 'es'),
            ('Inglés', 'en'),
            ('Francés', 'fr'),
            ('Alemán', 'de'),
            ('Italiano', 'it'),
            ('Portugués', 'pt'),
            ('Japonés', 'ja')
        ]
        
        # Crear widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Marco principal
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Entrada de texto
        ttk.Label(main_frame, text="Introduce tu texto:").pack(anchor=tk.W)
        self.text_input = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, height=8)
        self.text_input.pack(fill=tk.X, pady=5)
        
        # Marco de controles
        controls_frame = ttk.Frame(main_frame)
        controls_frame.pack(fill=tk.X, pady=5)
        
        # Selección de idioma
        ttk.Label(controls_frame, text="Idioma:").grid(row=0, column=0, sticky=tk.W)
        self.idioma_var = tk.StringVar()
        self.idioma_combobox = ttk.Combobox(controls_frame, 
                                          textvariable=self.idioma_var,
                                          values=[nombre for nombre, codigo in self.idiomas],
                                          state='readonly')
        self.idioma_combobox.current(0)
        self.idioma_combobox.grid(row=0, column=1, padx=5)
        
        # Velocidad de habla
        self.slow_var = tk.BooleanVar()
        ttk.Checkbutton(controls_frame, 
                      text="Hablado lento", 
                      variable=self.slow_var).grid(row=0, column=2, padx=10)
        
        # Ruta de guardado
        ttk.Label(main_frame, text="Archivo de salida:").pack(anchor=tk.W)
        self.file_frame = ttk.Frame(main_frame)
        self.file_frame.pack(fill=tk.X)
        
        self.file_path = tk.StringVar()
        self.file_entry = ttk.Entry(self.file_frame, textvariable=self.file_path)
        self.file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,5))
        
        ttk.Button(self.file_frame, 
                 text="Examinar...", 
                 command=self.select_file).pack(side=tk.LEFT)
        
        # Botones de acción
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(pady=10)
        
        ttk.Button(buttons_frame, 
                 text="Generar MP3", 
                 command=self.generate_audio).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(buttons_frame, 
                 text="Reproducir", 
                 command=self.play_audio).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(buttons_frame, 
                 text="Cargar texto desde archivo", 
                 command=self.load_text_file).pack(side=tk.LEFT, padx=5)
        
        # Estado
        self.status_var = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.status_var).pack(anchor=tk.W)
        
    def get_lang_code(self):
        for nombre, codigo in self.idiomas:
            if nombre == self.idioma_var.get():
                return codigo
        return 'es'
    
    def select_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".mp3",
            filetypes=[("Archivos MP3", "*.mp3")],
            title="Guardar audio como"
        )
        if file_path:
            self.file_path.set(file_path)
    
    def generate_audio(self):
        texto = self.text_input.get("1.0", tk.END).strip()
        if not texto:
            messagebox.showwarning("Error", "Por favor introduce algún texto")
            return
        
        file_path = self.file_path.get()
        if not file_path:
            messagebox.showwarning("Error", "Selecciona una ubicación para guardar el archivo")
            return
        
        try:
            tts = gTTS(
                text=texto,
                lang=self.get_lang_code(),
                slow=self.slow_var.get()
            )
            tts.save(file_path)
            self.status_var.set(f"Archivo generado exitosamente: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el audio: {str(e)}")
            self.status_var.set("Error al generar el archivo")
    
    def play_audio(self):
        file_path = self.file_path.get()
        if not os.path.exists(file_path):
            messagebox.showwarning("Error", "Primero genera el archivo de audio")
            return
        
        try:
            # Reproducir con reproductor predeterminado
            os.system(f'start "{file_path}"')  # Windows
            # Para Linux: usar 'xdg-open'
            # Para macOS: usar 'open'
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo reproducir el audio: {str(e)}")
    
    def load_text_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Archivos de texto", "*.txt")]
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    texto = f.read()
                self.text_input.delete("1.0", tk.END)
                self.text_input.insert("1.0", texto)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()