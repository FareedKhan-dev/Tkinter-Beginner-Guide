from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('My App')
root.iconbitmap('logo.ico')


my_img = ImageTk.PhotoImage(Image.open('logo.png'))
my_label = Label(image=my_img, width=40, height=50)
my_label.pack()







button_quit = Button(root, text='Quit it', padx=10, pady=10, command=root.quit)



button_quit.pack()

root.mainloop() 