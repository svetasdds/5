import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

class LabApp:
    def __init__(self, root):
        self.root = root
        self.root.title("lab4_2-320-v11-Ivanov-Ivan")

        # Initial Parameters
        self.steps_var = tk.IntVar(value=50)
        self.T_var = tk.DoubleVar(value=1.0)
        self.K_var = tk.DoubleVar(value=1.5)
        self.xi_var = tk.DoubleVar(value=0.1)
        self.T0_var = tk.DoubleVar(value=0.1)
        self.U_var = tk.DoubleVar(value=0.1)

        # GUI Layout
        self.create_widgets()

    def create_widgets(self):
        # Input parameters
        tk.Label(self.root, text="Number of steps:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.steps_var).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="T:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.T_var).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.root, text="K:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.K_var).grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.root, text="xi (\u03be):").grid(row=3, column=0, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.xi_var).grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.root, text="T0:").grid(row=4, column=0, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.T0_var).grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.root, text="U (initial input):").grid(row=5, column=0, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.U_var).grid(row=5, column=1, padx=5, pady=5)

        # Buttons
        tk.Button(self.root, text="Plot Data", command=self.plot_data).grid(row=6, column=0, columnspan=2, pady=10)

        # Result Label
        self.result_label = tk.Label(self.root, text="Results will be shown on the plot.")
        self.result_label.grid(row=7, column=0, columnspan=2, pady=10)

    def calculate_y(self, steps, T, K, xi, T0, U):
        """Calculate y[k] based on the recurrence relation."""
        y = np.zeros(steps)
        y[0] = U  # Initial condition
        y[1] = 0

        for k in range(steps - 2):
            term1 = (2 - (2 * xi * T0 / T)) * y[k + 1]
            term2 = ((2 * xi * T0 / T) - 1 - (T0**2 / T**2)) * y[k]
            term3 = (K * T0**2 / T**2) * U
            y[k + 2] = term1 + term2 + term3

        return y

    def plot_data(self):
        """Plots the calculated data using matplotlib."""
        try:
            steps = self.steps_var.get()
            T = self.T_var.get()
            K = self.K_var.get()
            xi = self.xi_var.get()
            T0 = self.T0_var.get()
            U = self.U_var.get()

            y = self.calculate_y(steps, T, K, xi, T0, U)
            t = np.arange(steps)

            plt.figure("Function Plot")
            plt.plot(t, y, label="y[k]", marker="o")
            plt.title("Recurrence Relation Plot")
            plt.xlabel("k (steps)")
            plt.ylabel("y[k]")
            plt.grid(True)
            plt.legend()
            plt.show()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to plot data: {e}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LabApp(root)
    root.mainloop()
