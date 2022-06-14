from email.policy import default
from optparse import Option
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

from sklearn.preprocessing import scale
from sklearn.utils import check_array

root = Tk()
root.title('My App')
root.iconbitmap('logo.ico')


option = ["Monday", "Tuesday","Wednesday", "Thursday", "Friday"]

clicked = StringVar()
clicked.set(option[0])


drop = OptionMenu(root, clicked, *option).pack()

def tester():
    Label(root, text=clicked.get()).pack()




print(drop)
Button(root, text='Click Me', command=tester).pack()



root.mainloop() 