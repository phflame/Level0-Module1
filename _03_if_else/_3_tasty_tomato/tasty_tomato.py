from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk
window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
TC = simpledialog.askstring(title='Tomato Question', prompt='What color tomato would you like. The options are red, green, and blue')
# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
if TC == "red":
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="red", outline="")
if TC == "green":
    canvas.create_oval(75, 200, 400, 450, fill="green", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="green", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
if TC == "blue":
    canvas.create_oval(75, 200, 400, 450, fill="blue", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="blue", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="blue", outline="")
if TC != "red" and TC != "green" and TC != "blue":

    canvas.create_text(300, 100, text="That was not one of the options.", fill="black")


root.mainloop()
