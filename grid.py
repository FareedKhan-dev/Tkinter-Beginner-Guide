from tkinter import * 


root = Tk()

# Creating a label widget
mylabel = Label(root, text='In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content.')

# Creating a label widget
mylabel2 = Label(root, text='In publishing and graphic design, how old are you, are you ok or not ok!')


mylabel.grid(row=0, column=0)
mylabel2.grid(row=1, column=5)


root.mainloop()