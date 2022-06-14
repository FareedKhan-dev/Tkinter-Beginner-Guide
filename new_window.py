from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('My App')
root.iconbitmap('logo.ico')

def window_open():
    global my_img1
    top = Toplevel()
    my_img1 = ImageTk.PhotoImage(Image.open('images/1.jpg').resize( [int(0.5 * s) for s in Image.open('images/1.jpg').size] ))
    my_label = Label(top, image=my_img1).pack()
    Button(top, text='close', command=top.destroy).pack()


mybutton = Button(root, text='open this window', command=window_open)

mybutton.pack()
root.mainloop() 