import tkinter as tk
from tkinter import messagebox

class DoubleFactorialApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Double Factorial Calculator")

        # GUI Elements
        self.label = tk.Label(root, text="Enter 5 integers separated by commas:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.pack(pady=10)

        self.result_label = tk.Label(root, text="Results will appear here.", wraplength=300)
        self.result_label.pack(pady=10)

    @staticmethod
    def fact2(N):
        if N <= 0:
            return 1
        result = 1
        step = 2 if N % 2 == 0 else 1
        for i in range(step, N + 1, 2):
            result *= i
        return result

    def calculate(self):
        try:
            input_text = self.entry.get()
            numbers = list(map(int, input_text.split(",")))
            if len(numbers) != 5:
                raise ValueError("Please enter exactly 5 integers.")

            results = [self.fact2(n) for n in numbers]
            result_text = "Double factorials: " + ", ".join(map(str, results))
            self.result_label.config(text=result_text)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

# Create the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DoubleFactorialApp(root)
    root.mainloop()
