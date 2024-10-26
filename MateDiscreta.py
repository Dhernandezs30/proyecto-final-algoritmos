from tkinter import Tk, Label, Entry, Button, IntVar, Radiobutton, messagebox, Frame
from math import factorial

def combinaciones(n, r, repeticion=False):
    if repeticion:
        return factorial(n + r - 1) // (factorial(r) * factorial(n - 1))
    else:
        if r > n:
            return 0
        return factorial(n) // (factorial(r) * factorial(n - r))

def permutaciones(n, r, repeticion=False):
    if repeticion:
        return n ** r
    else:
        if r > n:
            return 0
        return factorial(n) // factorial(n - r)

def calcular():
    n = n_var.get()
    r = r_var.get()
    repeticion = repeticion_var.get()

    if opcion_var.get() == 1:
        resultado = combinaciones(n, r, repeticion)
        messagebox.showinfo("Resultado", f"El resultado de las combinaciones es: {resultado}")
    elif opcion_var.get() == 2:
        resultado = permutaciones(n, r, repeticion)
        messagebox.showinfo("Resultado", f"El resultado de las permutaciones es: {resultado}")
    else:
        messagebox.showerror("Error", "Opción no válida.")

# Crear la ventana principal
root = Tk()
root.title("Calculadora de Combinaciones y Permutaciones")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# Variables
n_var = IntVar()
r_var = IntVar()
repeticion_var = IntVar()
opcion_var = IntVar()

# Frame para organización
frame = Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

# Labels y Entradas
Label(frame, text="Ingresa el valor de n:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", padx=10, pady=5)
Entry(frame, textvariable=n_var).grid(row=0, column=1, padx=10, pady=5)

Label(frame, text="Ingresa el valor de r:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", padx=10, pady=5)
Entry(frame, textvariable=r_var).grid(row=1, column=1, padx=10, pady=5)

Label(frame, text="¿Con repetición?", bg="#f0f0f0").grid(row=2, column=0, sticky="w", padx=10, pady=5)
Radiobutton(frame, text="Sí", variable=repeticion_var, value=1, bg="#f0f0f0").grid(row=2, column=1, sticky="w")
Radiobutton(frame, text="No", variable=repeticion_var, value=0, bg="#f0f0f0").grid(row=2, column=2, sticky="w")

# Opciones
Label(frame, text="Selecciona una opción:", bg="#f0f0f0").grid(row=3, column=0, sticky="w", padx=10, pady=5)
Radiobutton(frame, text="Combinaciones", variable=opcion_var, value=1, bg="#f0f0f0").grid(row=3, column=1, sticky="w")
Radiobutton(frame, text="Permutaciones", variable=opcion_var, value=2, bg="#f0f0f0").grid(row=3, column=2, sticky="w")

# Botón de calcular
Button(frame, text="Calcular", command=calcular, bg="#4CAF50", fg="white").grid(row=4, columnspan=3, pady=20)

# Iniciar la aplicación
root.mainloop()