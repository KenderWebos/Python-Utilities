import tkinter as tk
from fpdf import FPDF

def generar_pdf():
    # Obtener el texto ingresado en el formulario
    texto = text_box.get("1.0", tk.END).strip()

    if not texto:
        print("Por favor ingrese texto.")
        return

    # Crear una instancia de FPDF
    pdf = FPDF()

    # Agregar una página al PDF
    pdf.add_page()

    # Establecer fuente
    pdf.set_font("Arial", size=12)

    # Agregar el texto al PDF
    pdf.multi_cell(0, 10, texto)

    # Guardar el archivo PDF
    pdf.output("output.pdf")

    print("PDF generado con éxito.")

# Crear la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Generador de PDF")

# Crear un cuadro de texto donde se puede pegar el texto
text_box = tk.Text(ventana, height=15, width=50)
text_box.pack(padx=10, pady=10)

# Crear un botón que llame a la función para generar el PDF
boton_generar = tk.Button(ventana, text="Generar PDF", command=generar_pdf)
boton_generar.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()
