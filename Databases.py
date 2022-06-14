from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('My App')
root.iconbitmap('logo.ico')

# create database connect
conn = sqlite3.connect('address_book.db')

# create cursor
c = conn.cursor()

# create table
# c.execute("""CREATE TABLE addresses (

#     first_name text,
#     last_name text,
#     age integer,
#     city text

# )
# """)

first_name = Entry(root, width=50)
last_name = Entry(root, width=50)
age = Entry(root, width=50)
city = Entry(root, width=50)
first_name.pack()
last_name.pack()
age.pack()
city.pack()

first_name.insert(0, "Enter your First name")
last_name.insert(0, "Enter your last name")
age.insert(0, "Enter your age")
city.insert(0, "Enter your city")




# commit changes
conn.commit()


# closing connection
conn.close()

root.mainloop() 