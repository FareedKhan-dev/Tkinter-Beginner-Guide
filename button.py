from os import stat
from tkinter import *
from turtle import onclick 


root = Tk()

# Function to action of button
def myClick():
    mylabel = Label(root, text="Look! I clicked a button!!", fg='blue')
    mylabel.pack()


# Creating a button
# myButton = Button(root, text='Click Me', state=DISABLED)


# Creating a button
myButton = Button(root, text='Click Me', pady=50, padx=50, command=myClick, fg='blue', bg='#000')


myButton.pack()

root.mainloop()