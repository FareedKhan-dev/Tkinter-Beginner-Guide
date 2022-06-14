from glob import glob
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('My App')
root.iconbitmap('logo.ico')


def open_image():
    global my_img1
    root.filename = filedialog.askopenfilename(initialdir='C:/Users/faree/Desktop/tkinter/Images', title='Title of the box', filetypes=(("jpg files", '*.jpg*'),))

    my_img1 = ImageTk.PhotoImage(Image.open(root.filename).resize( [int(0.5 * s) for s in Image.open(root.filename).size] ))
    my_label = Label(root, image=my_img1).pack()

    # Label(root, text=root.filename).pack()

Button(root, text='Open an Image', command=open_image).pack()
root.mainloop() 