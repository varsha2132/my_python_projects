import sqlite3
from tkinter import *
from tkinter import messagebox
import math

class ScientificCalculatorGUI():
    def __init__(self, master):
        self.master = master
        self.num1 = DoubleVar()
        self.num2 = DoubleVar()
        self.result = StringVar()

        self.master.title('Scientific Calculator')
        self.master.geometry('400x300')

        self.label_num1 = Label(self.master, text="Enter Number 1:")
        self.label_num1.pack()

        self.entry_num1 = Entry(self.master, textvariable=self.num1)
        self.entry_num1.pack()

        self.label_num2 = Label(self.master, text="Enter Number 2:")
        self.label_num2.pack()

        self.entry_num2 = Entry(self.master, textvariable=self.num2)
        self.entry_num2.pack()

        self.operation_label = Label(self.master, text="Choose Operation:")
        self.operation_label.pack()

        self.operation_var = StringVar()
        self.operation_var.set("+")

        self.operations_menu = OptionMenu(self.master, self.operation_var, "+", "-", "*", "/", "sqrt", "^")
        self.operations_menu.pack()

        self.calculate_button = Button(self.master, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = Label(self.master, textvariable=self.result)
        self.result_label.pack()

    def calculate(self):
        try:
            num1 = self.num1.get()
            num2 = self.num2.get()
            operation = self.operation_var.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    messagebox.showerror("Error", "Cannot divide by zero.")
                    return
                result = num1 / num2
            elif operation == "sqrt":
                if num1 < 0:
                    messagebox.showerror("Error", "Cannot calculate square root of a negative number.")
                    return
                result = math.sqrt(num1)
            elif operation == "^":
                result = num1 ** num2
            else:
                messagebox.showerror("Error", "Invalid operation.")
                return

            self.result.set("Result: " + str(result))

            # Save calculation history to SQLite
            with sqlite3.connect("calculation_history.db") as db:
                cursor = db.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS history(Calculation TEXT NOT NULL);")
                cursor.execute("INSERT INTO history(Calculation) VALUES(?);", (f"{num1} {operation} {num2} = {result}",))
                db.commit()

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    root = Tk()
    app = ScientificCalculatorGUI(root)
    root.mainloop()
