"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""


from tkinter import messagebox, simpledialog, Tk

score = 0


A1 = simpledialog.askstring(title="Riddle #1", prompt="What has a head and a tail, but no body or legs??")

A2 = simpledialog.askstring(title="Riddle #2", prompt="What has many words but never speaks?")

A3 = simpledialog.askstring(title="Riddle #3", prompt="Which word in the dictionary is spelled incorrectly")


