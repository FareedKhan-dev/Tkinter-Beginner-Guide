from tkinter import *
from turtle import forward, right, width
from PIL import ImageTk, Image

root = Tk()
root.title('My App')
root.iconbitmap('logo.ico')

myframe = LabelFrame(root, text='This is my Frame....', padx=50, pady=50)
myframe.pack(padx=100, pady=100)

b = Button(myframe, text='My button in Frame', command=root.quit)
b.grid(row=0, column=0)

b2 = Button(myframe, text='My Second button in Frame', command=root.quit)
b2.grid(row=0, column=1)

root.mainloop() 