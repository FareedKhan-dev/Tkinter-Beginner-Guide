from os import stat
from tkinter import *
from turtle import onclick 


root = Tk()


e = Entry(root, width=50, bg='blue', borderwidth=5)
e.pack()
e.insert(0, "Enter your name")

# Function to action of button
def myClick():
    mylabel = Label(root, text=e.get(), fg='blue')
    mylabel.pack()


# Creating a button
# myButton = Button(root, text='Click Me', state=DISABLED)


# Creating a button
myButton = Button(root, text='Click Me', pady=50, padx=50, command=myClick, fg='blue', bg='#000')

 
myButton.pack()

root.mainloop() 