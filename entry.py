# Start building a button and UI for Input
#
from tkinter import *
from SolvePuzzle import solvePuzzle

root = Tk()

e1 = Entry(root, width=100)  # fg = text, bg = Box color
e2 = Entry(root, width=100)  # fg = text, bg = Box color

e1.pack()
e1.get()

e2.pack()
e2.get()
# e.insert(0, "Enter Your Name: ") # Prefill text box


def myClick():
    answers = solvePuzzle(e1.get(), e2.get())
    mylabel = Label(root, text=answers)
    mylabel.pack()


myButton = Button(root, text="Enter 7 distinct letters: ", command=myClick)
myButton.pack()


root.mainloop()
