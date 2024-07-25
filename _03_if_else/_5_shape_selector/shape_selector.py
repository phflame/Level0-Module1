import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    ekim = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    A1 = simpledialog.askstring(title="shapes", prompt="What shape do you want to draw? The options are triangle, square or circle.")
    ekim.goto(0, 0)
    # Draw the shape requested by the user using if-elif-else statements
    if A1 == "triangle":
        ekim.forward(50)
        ekim.left(120)
        ekim.forward(100)
        ekim.left(120)
        ekim.forward(100)
        ekim.left(120)
        ekim.forward(50)
    if A1 == "circle":
        ekim.circle(radius=100)
    if A1 == "square":

        ekim.forward(100)
        for i in range (3):
            ekim.left(90)
            ekim.forward(200)
        ekim.left(90)
        ekim.forward(100)



    turtle.done()
    # Call the turtle .done() method
