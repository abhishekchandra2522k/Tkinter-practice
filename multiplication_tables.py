import sys

from tkinter import *

def multiples():
    print("\n")

    for x in range(1,13):
        m = int(EnterTable.get())
        print("\t", (x), ' x ', (m), "=", (x * m))


Multiply = Tk()
Multiply.geometry('250x250+700+200')
Multiply.title('Multiplication Table')

EnterTable = StringVar()

label1 = Label(Multiply, text="Multiplication Table", font=30, fg = 'Black').grid(row=1,column=6)
label1 = Label(Multiply, text="                      ", font=30, fg = 'Black').grid(row=2,column=6)
enrty1 = Entry(Multiply,textvariable=EnterTable, justify=CENTER).grid(row=3, column=6)
label1 = Label(Multiply, text="                      ", font=30, fg = 'Black').grid(row=4,column=6)

button1 =  Button(Multiply, text="Multiplication Table", command=multiples).grid(row=5, column=6)
label1 = Label(Multiply, text="                     ").grid(row=6, column=6)
QUIT = Button(Multiply, text="Quit", fg="Red", command=Multiply.destroy).grid(row=7, column=6)

Multiply.mainloop()