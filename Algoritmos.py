import tkinter as tk
from tkinter import messagebox
import numpy as np
import ast

# Funciones para cada apartado
def regresar_inicio(ventana):
    ventana.destroy()

def abrir_algebra():
    ventana_algebra = tk.Toplevel()
    ventana_algebra.title("Álgebra Lineal")
    
    etiqueta = tk.Label(ventana_algebra, text="Sección de Álgebra Lineal", font=("Arial", 14, "bold"))
    etiqueta.pack(padx=20, pady=20)
    
    descripcion = tk.Label(ventana_algebra, text="Aquí puedes resolver problemas de espacios vectoriales, matrices, transformaciones lineales, etc.", font=("Arial", 12))
    descripcion.pack(padx=10, pady=10)
    
    btn_regresar = tk.Button(ventana_algebra, text="Regresar", command=lambda: regresar_inicio(ventana_algebra))
    btn_regresar.pack(pady=20)

def abrir_algoritmos():
    ventana_algoritmos = tk.Toplevel()
    ventana_algoritmos.title("Algoritmos")

    etiqueta = tk.Label(ventana_algoritmos, text="Sección de Algoritmos", font=("Arial", 14, "bold"))
    etiqueta.pack(padx=20, pady=10)

    # Aquí va el código específico de operaciones de matrices
    # Funciones matemáticas
    def gauss_jordan(matrix):
        try:
            matrix = np.array(matrix, dtype=float)
            rows, cols = matrix.shape
            for i in range(min(rows, cols)):
                matrix[i] = matrix[i] / matrix[i][i]  # Dividir fila por el elemento diagonal
                for j in range(rows):
                    if i != j:
                        matrix[j] = matrix[j] - matrix[i] * matrix[j][i]
            return matrix
        except Exception as e:
            return f"Error en Gauss-Jordan: {e}"

    def cramer(matrix, constants):
        try:
            matrix = np.array(matrix)
            constants = np.array(constants)
            det_matrix = np.linalg.det(matrix)
            if det_matrix == 0:
                return "El sistema no tiene solución única (determinante = 0)"
            solutions = []
            for i in range(matrix.shape[1]):
                matrix_copy = matrix.copy()
                matrix_copy[:, i] = constants
                solutions.append(np.linalg.det(matrix_copy) / det_matrix)
            return solutions
        except Exception as e:
            return f"Error en Cramer: {e}"

    def multiply_matrices(matrix1, matrix2):
        try:
            matrix1 = np.array(matrix1)
            matrix2 = np.array(matrix2)
            return np.dot(matrix1, matrix2)
        except ValueError as e:
            return f"Error en la multiplicación: {e}"

    def inverse_matrix(matrix):
        try:
            matrix = np.array(matrix)
            return np.linalg.inv(matrix)
        except np.linalg.LinAlgError:
            return "La matriz no tiene inversa (determinante = 0)"
        except Exception as e:
            return f"Error al calcular la inversa: {e}"

    # Función para convertir la entrada de texto en una matriz
    def parse_matrix(input_str):
        try:
            matrix = ast.literal_eval(input_str)
            if isinstance(matrix, list):
                return matrix
            else:
                raise ValueError("Entrada inválida. Usa el formato: [[1,2],[3,4]]")
        except Exception as e:
            raise ValueError(f"Entrada inválida: {e}")

    def perform_operation():
        method = method_var.get()
        try:
            matrix = parse_matrix(matrix_entry.get())
            if method == 'Gauss-Jordan':
                result = gauss_jordan(matrix)
            elif method == 'Regla de Cramer':
                constants = parse_matrix(constants_entry.get())
                result = cramer(matrix, constants)
            elif method == 'Multiplicación':
                matrix2 = parse_matrix(matrix2_entry.get())
                result = multiply_matrices(matrix, matrix2)
            elif method == 'Inversa':
                result = inverse_matrix(matrix)
            show_result(result)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Función para mostrar los resultados
    def show_result(result):
        result_window = tk.Toplevel()
        result_window.title("Resultado")
        result_text = tk.Text(result_window)
        result_text.insert(tk.END, str(result))
        result_text.pack()

    # Crear la interfaz gráfica
    tk.Label(ventana_algoritmos, text="Matriz (usa formato Python, e.g. [[1,2],[3,4]])").pack(pady=5)
    matrix_entry = tk.Entry(ventana_algoritmos)
    matrix_entry.pack(pady=5)

    tk.Label(ventana_algoritmos, text="Constantes (para Cramer)").pack(pady=5)
    constants_entry = tk.Entry(ventana_algoritmos)
    constants_entry.pack(pady=5)

    tk.Label(ventana_algoritmos, text="Segunda matriz (para multiplicación)").pack(pady=5)
    matrix2_entry = tk.Entry(ventana_algoritmos)
    matrix2_entry.pack(pady=5)

    method_var = tk.StringVar(ventana_algoritmos)
    method_var.set("Gauss-Jordan")

    tk.Label(ventana_algoritmos, text="Método").pack(pady=5)
    method_menu = tk.OptionMenu(ventana_algoritmos, method_var, "Gauss-Jordan", "Regla de Cramer", "Multiplicación", "Inversa")
    method_menu.pack(pady=5)

    execute_button = tk.Button(ventana_algoritmos, text="Calcular", command=perform_operation)
    execute_button.pack(pady=5)

    # Botón para regresar
    btn_regresar = tk.Button(ventana_algoritmos, text="Regresar", command=lambda: regresar_inicio(ventana_algoritmos))
    btn_regresar.pack(pady=20)

def abrir_matematica_discreta():
    ventana_matematica_discreta = tk.Toplevel()
    ventana_matematica_discreta.title("Matemática Discreta")
    ventana_matematica_discreta.geometry("400x400")
    ventana_matematica_discreta.config(bg="#f0f0f0")
    
    # Variables
    n_var = tk.IntVar()
    r_var = tk.IntVar()
    repeticion_var = tk.IntVar()
    opcion_var = tk.IntVar()

    # Frame para organización
    frame = tk.Frame(ventana_matematica_discreta, bg="#f0f0f0")
    frame.pack(pady=20)

    # Labels y Entradas
    tk.Label(frame, text="Ingresa el valor de n:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    tk.Entry(frame, textvariable=n_var).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame, text="Ingresa el valor de r:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    tk.Entry(frame, textvariable=r_var).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame, text="¿Con repetición?", bg="#f0f0f0").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    tk.Radiobutton(frame, text="Sí", variable=repeticion_var, value=1, bg="#f0f0f0").grid(row=2, column=1, sticky="w")
    tk.Radiobutton(frame, text="No", variable=repeticion_var, value=0, bg="#f0f0f0").grid(row=2, column=2, sticky="w")

    # Opciones
    tk.Label(frame, text="Selecciona una opción:", bg="#f0f0f0").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    tk.Radiobutton(frame, text="Combinaciones", variable=opcion_var, value=1, bg="#f0f0f0").grid(row=3, column=1, sticky="w")
    tk.Radiobutton(frame, text="Permutaciones", variable=opcion_var, value=2, bg="#f0f0f0").grid(row=3, column=2, sticky="w")

    # Función para calcular combinaciones o permutaciones
    def calcular():
        try:
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
                messagebox.showwarning("Advertencia", "Selecciona una opción válida.")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

    # Botón para calcular
    btn_calcular = tk.Button(ventana_matematica_discreta, text="Calcular", command=calcular)
    btn_calcular.pack(pady=20)

    # Botón para regresar
    btn_regresar = tk.Button(ventana_matematica_discreta, text="Regresar", command=lambda: regresar_inicio(ventana_matematica_discreta))
    btn_regresar.pack(pady=20)

# Ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Proyecto Final")
ventana_principal.geometry("400x350")
ventana_principal.config(bg="#f0f0f0")

# Etiqueta principal
titulo = tk.Label(ventana_principal, text="Proyecto Final de", font=("Arial", 18, "bold"), bg="#f0f0f0")
titulo.pack(pady=10)

subtitulo = tk.Label(ventana_principal, text="Álgebra Lineal, Algoritmos y Matemática Discreta", font=("Arial", 12), bg="#f0f0f0")
subtitulo.pack(pady=5)

# Botones para cada apartado con colores personalizados
btn_algebra = tk.Button(ventana_principal, text="Álgebra Lineal", command=abrir_algebra, 
                        width=25, height=2, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_algebra.pack(pady=10)

btn_algoritmos = tk.Button(ventana_principal, text="Algoritmos", command=abrir_algoritmos, 
                           width=25, height=2, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
btn_algoritmos.pack(pady=10)

btn_matematica_discreta = tk.Button(ventana_principal, text="Matemática Discreta", command=abrir_matematica_discreta, 
                                    width=25, height=2, bg="#FF5722", fg="white", font=("Arial", 10, "bold"))
btn_matematica_discreta.pack(pady=10)

# Etiqueta para los nombres en la parte inferior derecha
nombres = tk.Label(ventana_principal, text="Jhonny Peralta\nAbraham Rodriguez\nDylan Hernandez", 
                   font=("Arial", 10), bg="#f0f0f0", anchor="e")  # 'anchor' para alinear a la derecha
nombres.place(relx=1.0, rely=1.0, anchor='se')  # 'se' es sureste (suroeste)

# Ejecutar la ventana principal
ventana_principal.mainloop()
