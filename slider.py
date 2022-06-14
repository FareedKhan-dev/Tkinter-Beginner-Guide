from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

from sklearn.preprocessing import scale

root = Tk()
root.title('My App')
root.iconbitmap('logo.ico')


scalevar = IntVar()
scalevar.set(50)

# vertical_scale = Scale(root, from_=0, to=200)
# vertical_scale.pack()



horizontal_scale = Scale(root, from_=0, to=200,  variable=scalevar,orient=HORIZONTAL)
horizontal_scale.pack()

Label(root, textvariable=scalevar).pack()

# root.geometry(str(scalevar) + "x400")
root.mainloop() 