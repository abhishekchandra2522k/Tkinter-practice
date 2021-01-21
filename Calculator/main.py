from tkinter import *
from tkinter import ttk

# some useful variables
fnt = ('Verdana', 22)


# creating a window
root = Tk()

root.title('Calculator')
root.geometry('400x500')

#picture label
pic = PhotoImage(file='Calculator/images/64x64.png')
heading = Label(root, image=pic).pack(side=TOP, pady=10)

#heading label
headingLabel = Label(root ,text='Calculator', font=fnt).pack(side=TOP)


# text field (user input)
textField = Entry(root, font=fnt).pack()

root.mainloop()