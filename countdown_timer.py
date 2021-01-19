from tkinter import *
from tkinter import ttk
from tkinter import font

import time
import datetime

root = Tk()
# Tk() creates a route, so everything we put on screen whether it is a textbox, button or an image 
# is referred to a widget and they must all be placed in the route.
# Think of a route as a basket that we put all our widgets in.

Label(root, text="Time until 20th Jan, 2021").pack()

global endTime 

# when we are not sure how many arguments might be passed to our function, we use (*args)
def quit(*args):
    '''This function is used to quit the tkinter GUI application'''
    root.destroy()


def cant_wait():
    '''Get the time remaining until an event'''
    timeLeft = endTime - datetime.datetime.now()

    # remove the microseconds part
    timeLeft = timeLeft - datetime.timedelta(microseconds=timeLeft.microseconds)

    #show the time left
    txt.set(timeLeft)

    # Trigger the countdown after 1000ms
    root.after(1000,cant_wait)


# Use tkinter lib for showing the clock
root.attributes("-fullscreen",False)

root.configure(background='yellow')

root.bind('x',quit)

root.after(1000,cant_wait)

# set the end date and time for the countdown
endTime = datetime.datetime(2021,1,20,0,0)

fnt = font.Font(family='Helvetica', size=90, weight='bold')

txt = StringVar()

lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground='black', background='yellow')

lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()