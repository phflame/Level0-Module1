import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    R1 = simpledialog.askinteger(title='Cicle Area Calculator', prompt='Give me the radius of a circle and I can give you the area. Choose a radius between 1-200')
    # Make a new turtle
    ekim = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    ekim.circle(radius=R1)
    # Call the turtle .penup() method
    ekim.penup()
    # Move your turtle to a new x,y position using .goto()
    ekim.goto(-100, -100)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area = math.pi*R1*R1
    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    ekim.write(arg="area = " + str(area) + " pixels", move=True, align='left', font=('Arial', 20, 'normal'))
    # Hide your turtle

    turtle.hideturtle()
    turtle.done()
    # Call turtle.done()
