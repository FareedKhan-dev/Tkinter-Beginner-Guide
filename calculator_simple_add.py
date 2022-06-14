from os import stat
from tkinter import *
from turtle import onclick, width

root = Tk()


# e = Entry(root, width=50, bg='blue', borderwidth=5)
# e.pack()
# e.insert(0, "Enter your name")

# # Function to action of button
# def myClick():
#     mylabel = Label(root, text=e.get(), fg='blue')
#     mylabel.pack()


# # Creating a button
# # myButton = Button(root, text='Click Me', state=DISABLED)


# # Creating a button
# myButton = Button(root, text='Click Me', pady=50, padx=50, command=myClick, fg='blue', bg='#000')

 
# myButton.pack()

root.title('Fareed Calculator')

e = Entry(root, width=45, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    # e.delete(0, END)
    current_num = e.get()
    e.delete(0, END)
    e.insert(0, str(current_num) + str(number))


def button_clear():
    e.delete(0,END)



def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0,END)

def button_equal(): 
    second_number = e.get()
    result = f_num + int(second_number)
    e.delete(0,END)
    e.insert(0, result)

myButton1 = Button(root, text='1',pady=20, padx=40, command=lambda: button_click(1))
myButton2 = Button(root, text='2',pady=20, padx=40, command=lambda: button_click(2))
myButton3 = Button(root, text='3',pady=20, padx=40, command=lambda: button_click(3))
myButton4 = Button(root, text='4',pady=20, padx=40, command=lambda: button_click(4))
myButton5 = Button(root, text='5',pady=20, padx=40, command=lambda: button_click(5))
myButton6 = Button(root, text='6',pady=20, padx=40, command=lambda: button_click(6))
myButton7 = Button(root, text='7',pady=20, padx=40, command=lambda: button_click(7))
myButton8 = Button(root, text='8',pady=20, padx=40, command=lambda: button_click(8))
myButton9 = Button(root, text='9',pady=20, padx=40, command=lambda: button_click(9))

myButtonadd = Button(root, text='+',pady=20, padx=91, command=lambda: button_add())
myButtonsub = Button(root, text='-',pady=20, padx=91, command=lambda: button_add())
myButtonmulti = Button(root, text='x',pady=20, padx=91, command=lambda: button_add())

myButtonequal = Button(root, text='=',pady=20, padx=40, command=lambda: button_equal())


myButtonclear = Button(root, text='clear', padx=140, pady=20 ,command=lambda: button_clear())


myButton1.grid(row=1,column=0)
myButton2.grid(row=1, column=1)
myButton3.grid(row=1, column=2) 
myButton4.grid(row=2, column=0)
myButton5.grid(row=2, column=1)
myButton6.grid(row=2, column=2)
myButton7.grid(row=3, column=0)
myButton8.grid(row=3, column=1)
myButton9.grid(row=3, column=2)
myButtonadd.grid(row=4, column=0, columnspan=2)
myButtonsub.grid(row=5, column=0, columnspan=1)
# myButtonmulti.grid(row=5, column=1, columnspan=2)
# myButtonclear.grid(row=7, column=1, columnspan=2)


myButtonequal.grid(row=4, column=2)


root.mainloop() 