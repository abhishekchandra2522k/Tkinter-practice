from tkinter import *

# Tk constructor is called with Tk() syntax in root variable.
root = Tk()  

# pack() method helps to display the text in a GUI window
Label (root, text = "Hello Tkinter!").pack()  

root.mainloop() 
# this will help the window to remain active until closed, 
# kind of an infinite loop is created so that application window didn't get closed immediately.

