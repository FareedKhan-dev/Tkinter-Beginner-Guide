from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('My App')
root.iconbitmap('logo.ico')

house_price = np.random.normal(2000, 3000, 5000)
plt.hist(house_price, 50)
plt.show()

root.mainloop() 