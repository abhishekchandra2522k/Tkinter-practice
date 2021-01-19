from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

def quit(*args):
    '''This function is used to quit the tkinter GUI application'''
    root.destroy()

def clock_time():
    time = datetime.datetime.now()
    
    # strftime function is used to format the time based on the arguments by user
    #time = (time.strftime("%H:%M:%S")) 
    time = (time.strftime("%d-%m-%Y %H:%M:%S"))

    txt.set(time)

    root.after(1000,clock_time)

root = Tk()

root.attributes("-fullscreen",False) # GUI will not be fullscreen, Use True in arg for fullscreen
root.configure(background='black')

root.bind('x',quit)

root.after(1000, clock_time)

fnt = font.Font(family='Helvetica', size=50, weight='bold')

txt = StringVar()

# Properties of the clock
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground='yellow', background='black')

# anchor parameter is used to anchor the widget to the center 
lbl.place(relx=0.5, rely=0.5, anchor=CENTER) 
# relx and rely are geometric functions used in tkinter to give a position 
# that is relative to the window


# this will keep the window and program (clock) running until the window is closed
root.mainloop() 