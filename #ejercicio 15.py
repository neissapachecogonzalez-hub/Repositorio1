#ejercicio 15 
#creado por:nestor enrique coria garcia

import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Actividad 15")
ventana.geometry("250x300")

# Etiqueta de texto
etiqueta = tk.Label(ventana,)
etiqueta.pack(pady=10)


# Cuadro de texto
nombre  = tk.Entry(ventana)
apellido =tk.Entry (ventana)
nombre.pack()
apellido.pack()

# funcion de mostrar el nombre
def mostrarnombre ():
    texto = nombre.get() + " " + apellido.get()
    etiqueta_resultado.config(text=f"{texto}")


# Etiqueta con resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="blue")
etiqueta_resultado.pack(pady=20)

# Boton de comando
boton = tk.Button(ventana,text="mostrar" ,command=mostrarnombre)
boton.pack(pady=20)


ventana.mainloop()