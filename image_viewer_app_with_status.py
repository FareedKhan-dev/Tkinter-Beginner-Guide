from tkinter import *
from turtle import forward, right, width
from PIL import ImageTk, Image

root = Tk()
root.title('My App')
root.iconbitmap('logo.ico')

half = 0.5


my_img1 = ImageTk.PhotoImage(Image.open('images/1.jpg').resize( [int(half * s) for s in Image.open('images/1.jpg').size] ))

my_img2 = ImageTk.PhotoImage(Image.open('images/2.jpg').resize( [int(half * s) for s in Image.open('images/1.jpg').size] ))

my_img3 = ImageTk.PhotoImage(Image.open('images/3.jpg').resize( [int(half * s) for s in Image.open('images/1.jpg').size] ))


my_img_list = [my_img1, my_img2, my_img3]

status = Label(root, text='Image 1 of ' + str(len(my_img_list)), pady=10, bd=1, relief=SUNKEN ) # anchor=E

my_label = Label(image=my_img1)
my_label.grid(row=0,column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    
    my_label = Label(image=my_img_list[image_number-1])


    button_forward = Button(root, text='>', command=lambda: forward(image_number+1))
    button_back = Button(root, text='<', command=lambda: back(image_number-1))

    if image_number == 3:
        button_forward = Button(root, text='>', state=DISABLED) 

    my_label.grid(row=0,column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    status = Label(root, text='Image ' + str(image_number) + ' of ' + str(len(my_img_list)), pady=10, bd=1, relief=SUNKEN ) # anchor=E
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

       

    



    
def back(image_number):
    global my_label
    global button_forward
    global button_back

    
    my_label.grid_forget()


    my_label = Label(image=my_img_list[image_number-1])


    button_forward = Button(root, text='>', command=lambda: forward(image_number+1))
    button_back = Button(root, text='<', command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text='<', state=DISABLED) 

    my_label.grid(row=0,column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    status = Label(root, text='Image ' + str(image_number) + ' of ' + str(len(my_img_list)), pady=10, bd=1, relief=SUNKEN ) # anchor=E
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    

button_back = Button(root, text='<', command=lambda: back)
button_forward = Button(root, text='>', command=lambda: forward(2))
button_exit = Button(root, text='Exit', command=root.quit)


button_back.grid(row=1,column=0)
button_forward.grid(row=1,column=2, pady=10)
button_exit.grid(row=1,column=1)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)



root.mainloop() 