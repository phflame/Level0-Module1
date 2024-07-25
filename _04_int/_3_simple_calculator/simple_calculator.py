"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""


from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    A1 = simpledialog.askinteger(title="calculator", prompt="This calculator can add, subtract, multiply, or divide any two integers. What is the first number you would like use.")

    A2 = simpledialog.askinteger(title="calculator", prompt="What is the second number you would like to use?")

    A4 = simpledialog.askstring(title="calculator", prompt="What operation would you like to do? The options are add, subtract, multiply and divide.")

    if A4 == "add":
        result = A1+A2
    if A4 == "multiply":
        result = A1*A2
    if A4 == "subtract":
        result = A1-A2
    if A4 == "divide":
        result = A1/A2
    if A4 != "divide" and A4 != "multiply" and A4 != "subtract" and A4 != "add":
        messagebox.showinfo(message="that wasn't one of the operations :(")
    else:

        messagebox.showinfo(message="The answer you get when you " + A4 + " " + str(A1) + " and " + str(A2) + " is " + str(result) + "." )


    messagebox.showinfo(message="The sum of the values: " + str(A1) + " and " + str(A2) + " is equal to " + str(A3) + ".")

