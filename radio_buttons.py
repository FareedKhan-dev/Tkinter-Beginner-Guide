from genericpath import exists
from msilib.schema import RadioButton
from multiprocessing import Value
from statistics import variance
from tkinter import *
from turtle import forward, right, width
from PIL import ImageTk, Image
from requests import options

root = Tk()
root.title('My App')
root.iconbitmap('logo.ico')

option = IntVar()
option.set(2)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()




for each_rad in range(0,10):
    Radiobutton(root, text='option ' + str(each_rad), variable=option, value=each_rad, command=lambda: clicked(option.get())).pack()


myLabel = Label(root, text=option.get())
myLabel.pack()

root.mainloop() 