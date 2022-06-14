from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('My App')
root.iconbitmap('logo.ico')


def pop_up():
    messagebox.showinfo('this is title', 'This is info Box')

def pop_up_error():
    messagebox.showerror('this is title', 'This is error Box')


def pop_up_warning():
    response = messagebox.showwarning('this is title', 'This is warning Box')
    print(response)


def pop_up_askquestion():
    response = messagebox.askquestion('this is title', 'This is to ask question?')
    print(response)

def pop_up_asktocancel():
    response = messagebox.askokcancel('this is title', 'This is to ask cancel')
    print(response)

def pop_up_asktoyesno():
    response = messagebox.askyesno('this is title', 'This is to ask yes or no')
    print(response)

mybutton1 = Button(root, text='Pop up my box', command=pop_up)
mybutton2 = Button(root, text='Pop up error', command=pop_up_error)
mybutton3 = Button(root, text='Pop up warning', command=pop_up_warning)
mybutton4 = Button(root, text='Pop up question', command=pop_up_askquestion)
mybutton5 = Button(root, text='Pop up to cancel', command=pop_up_asktocancel)
mybutton6 = Button(root, text='Pop up yes no', command=pop_up_asktoyesno)




mybutton1.pack()
mybutton2.pack()
mybutton3.pack()
mybutton4.pack()
mybutton5.pack()
mybutton6.pack()

root.mainloop() 