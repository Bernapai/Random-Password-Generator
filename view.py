# view.py

import tkinter as tk
import pyperclip  
from generator import generate_password  

# Función para actualizar la etiqueta con la nueva contraseña generada
def on_generate_password():
    password = generate_password()  
    password_label.config(text=f"Your password: {password}")
    global current_password  
    current_password = password

# Función para copiar la contraseña al portapapeles
def copiar():
    pyperclip.copy(current_password)  


root = tk.Tk()
root.title("Password Generator")


current_password = ''

# Configurar la etiqueta que mostrará la contraseña
password_label = tk.Label(root, text="Your password: ", font=("Helvetica", 14))
password_label.pack(pady=20)

# Crear el botón para generar la contraseña
generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 14), command=on_generate_password)
generate_button.pack(pady=10)

# Crear el botón para copiar la contraseña al portapapeles
copy_button = tk.Button(root, text="Copy to Clipboard", font=("Helvetica", 14), command=copiar)
copy_button.pack(pady=10)

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()
