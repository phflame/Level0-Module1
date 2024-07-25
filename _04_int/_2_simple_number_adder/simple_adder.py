"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""

from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    A1 = simpledialog.askinteger(title="calculator", prompt="This calculator can add any two integers. What is the first number you would like to add")

    A2 = simpledialog.askinteger(title="calculator", prompt="what is the second number you would like to add")

    A3 = A1+A2

    messagebox.showinfo(message="The sum of the values: " + str(A1) + " and " + str(A2) + " is equal to " + str(A3) + ".")

