import tkinter as tk
from tkinter import ttk, messagebox

class MatrixOperationsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Operaciones de Matrices")
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        self.create_inverse_matrix_tab()
        self.create_multiply_matrices_tab()
        self.create_solve_system_tab()
        self.create_plot_tab()

    def create_inverse_matrix_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Inversa de Matriz')
        
        self.inverse_matrix_input = tk.Text(frame, height=10, width=30)
        self.inverse_matrix_input.pack(pady=10)
        
        self.inverse_button = ttk.Button(frame, text='Calcular Inversa', command=self.calculate_inverse)
        self.inverse_button.pack(pady=10)
        
        self.inverse_result = tk.Label(frame, text='')
        self.inverse_result.pack(pady=10)

    def calculate_inverse(self):
        try:
            matrix = self.parse_matrix(self.inverse_matrix_input.get("1.0", tk.END))
            inverse_matrix = self.inverse(matrix)
            self.inverse_result.config(text=str(inverse_matrix))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def inverse(self, matrix):
        if len(matrix) != 2 or len(matrix[0]) != 2:
            raise ValueError("Solo se admite matrices 2x2")
        
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        if det == 0:
            raise ValueError("La matriz no tiene inversa")
        
        return [[matrix[1][1] / det, -matrix[0][1] / det],
                [-matrix[1][0] / det, matrix[0][0] / det]]

    def create_multiply_matrices_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Multiplicación de Matrices')
        
        self.matrix1_input = tk.Text(frame, height=10, width=30)
        self.matrix1_input.pack(pady=10)
        
        self.matrix2_input = tk.Text(frame, height=10, width=30)
        self.matrix2_input.pack(pady=10)

        self.multiply_button = ttk.Button(frame, text='Multiplicar', command=self.multiply_matrices)
        self.multiply_button.pack(pady=10)

        self.multiply_result = tk.Label(frame, text='')
        self.multiply_result.pack(pady=10)

    def multiply_matrices(self):
        try:
            matrix1 = self.parse_matrix(self.matrix1_input.get("1.0", tk.END))
            matrix2 = self.parse_matrix(self.matrix2_input.get("1.0", tk.END))
            result = self.multiply(matrix1, matrix2)
            self.multiply_result.config(text=str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def multiply(self, matrix1, matrix2):
        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Las matrices no se pueden multiplicar")
        
        result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        return result

    def create_solve_system_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Resolver Sistemas de Ecuaciones')
        
        self.system_input = tk.Text(frame, height=10, width=30)
        self.system_input.pack(pady=10)

        self.method_var = tk.StringVar(value='Gauss-Jordan')
        self.method_menu = ttk.OptionMenu(frame, self.method_var, 'Gauss-Jordan', 'Gauss-Jordan', 'Regla de Cramer')
        self.method_menu.pack(pady=10)

        self.solve_button = ttk.Button(frame, text='Resolver', command=self.solve_system)
        self.solve_button.pack(pady=10)

        self.solve_result = tk.Label(frame, text='')
        self.solve_result.pack(pady=10)

    def solve_system(self):
        try:
            equations = self.system_input.get("1.0", tk.END).strip().splitlines()
            coefficients = []
            constants = []

            for eq in equations:
                parts = eq.split('=')
                left = parts[0].strip()
                right = float(parts[1].strip())
                constants.append(right)
                coeff = [float(num) for num in left.replace('x', '').replace('y', '').replace(' ', '').split('+')]
                coefficients.append(coeff)

            if len(coefficients) == 2:
                result = self.solve_2x2(coefficients, constants)
            elif len(coefficients) == 3:
                result = self.solve_3x3(coefficients, constants)
            else:
                raise ValueError("Solo se admiten sistemas de 2x2 o 3x3")

            self.solve_result.config(text=f"Resultados: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def solve_2x2(self, coeffs, consts):
        a, b = coeffs
        d = a[0]*b[1] - a[1]*b[0]
        if d == 0:
            return "Sin solución o infinitas soluciones"
        
        x = (consts[0]*b[1] - consts[1]*b[0]) / d
        y = (a[0]*consts[1] - a[1]*consts[0]) / d
        return f"x = {x}, y = {y}"

    def solve_3x3(self, coeffs, consts):
        a, b, c = coeffs
        d = (a[0]*(b[1]*c[2] - b[2]*c[1]) - 
              a[1]*(b[0]*c[2] - b[2]*c[0]) + 
              a[2]*(b[0]*c[1] - b[1]*c[0]))
        
        if d == 0:
            return "Sin solución o infinitas soluciones"
        
        d1 = (consts[0]*(b[1]*c[2] - b[2]*c[1]) - 
              consts[1]*(b[0]*c[2] - b[2]*c[0]) + 
              consts[2]*(b[0]*c[1] - b[1]*c[0]))
        
        d2 = (a[0]*(consts[1]*c[2] - consts[2]*c[1]) - 
              a[1]*(consts[0]*c[2] - consts[2]*c[0]) + 
              a[2]*(consts[0]*c[1] - consts[1]*c[0]))
        
        d3 = (a[0]*(b[1]*consts[2] - b[2]*consts[1]) - 
              a[1]*(b[0]*consts[2] - b[2]*consts[0]) + 
              a[2]*(b[0]*consts[1] - b[1]*consts[0]))

        x = d1 / d
        y = d2 / d
        z = d3 / d
        
        return f"x = {x}, y = {y}, z = {z}"

    def create_plot_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Graficar Ecuaciones')
        
        self.plot_input = tk.Entry(frame)
        self.plot_input.pack(pady=10)

        self.plot_button = ttk.Button(frame, text='Graficar', command=self.plot_equation)
        self.plot_button.pack(pady=10)

        self.canvas = tk.Canvas(frame, width=400, height=400, bg='white')
        self.canvas.pack(pady=10)

    def plot_equation(self):
        equation = self.plot_input.get()
        self.canvas.delete("all")  # Limpiar el canvas antes de dibujar
        try:
            x_values = range(-10, 11)
            y_values = []
            for x in x_values:
                y = eval(equation.replace('x', str(x)))
                y_values.append(y)

            # Dibujar ejes
            self.canvas.create_line(200, 0, 200, 400, fill='black')  # Eje Y
            self.canvas.create_line(0, 200, 400, 200, fill='black')  # Eje X

            # Dibujar la gráfica
            for i in range(len(x_values) - 1):
                x1 = 200 + x_values[i] * 20  # Escalar x
                y1 = 200 - y_values[i] * 20  # Escalar y
                x2 = 200 + x_values[i + 1] * 20  # Escalar x
                y2 = 200 - y_values[i + 1] * 20  # Escalar y
                self.canvas.create_line(x1, y1, x2, y2, fill='blue')

            messagebox.showinfo("Resultados", "Gráfica dibujada en la ventana.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def parse_matrix(self, text):
        return [[float(num) for num in line.split()] for line in text.strip().splitlines()]

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixOperationsApp(root)
    root.mainloop()
