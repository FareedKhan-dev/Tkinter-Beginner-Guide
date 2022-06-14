from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

from sklearn.preprocessing import scale
from sklearn.utils import check_array

root = Tk()
root.title('My App')
root.iconbitmap('logo.ico')

my_var = IntVar()

c = Checkbutton(root, text='Check this box', variable=my_var)

c.pack()

def changing():
    Label(root, text=my_var.get()).pack()


myButton = Button(root, text='Click Me', command=changing).pack()

root.mainloop() 