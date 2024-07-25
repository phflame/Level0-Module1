# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk
import turtle
window_width = 600
window_height = 600
import math
if __name__ == '__main__':
    window = Tk()
    window.withdraw()


root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()


A1 = simpledialog.askinteger(title="circle calculator", prompt="What is the radius of the circle that you want to calculate.")
#Area = πr^2
#Circumference = 2πr
ekim = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
ekim.circle(radius=A1)
    # Call the turtle .penup() method
ekim.penup()
    # Move your turtle to a new x,y position using .goto()
ekim.goto(-100, -100)

A2 = simpledialog.askstring(title="circle calculator", prompt="Do you want to calculate the circumference or the area?")
circumference = math.pi*2*A1
area = math.pi*A1*A1
if A2 == "circumference":
    ekim.write(arg="circumference = " + str(circumference) + " pixels", move=True, align='left', font=('Arial', 20, 'normal'))
if A2 == "area":
    ekim.write(arg="Area = " + str(area) + " pixels", move=True, align='left', font=('Arial', 20, 'normal'))
if A2 != "area" and A2 != "circumference":
    messagebox.showinfo(message="that was not one of the options")


turtle.hideturtle()
turtle.done()
