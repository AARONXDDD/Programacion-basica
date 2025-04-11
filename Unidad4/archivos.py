import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "Hola Mundo - Interfaz Gráfica")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Gráfica")

# Crear un botón
boton = tk.Button(ventana, text="Presióname", command=mostrar_mensaje)
boton.pack(pady=20)

# Ejecutar el bucle principal
ventana.mainloop()