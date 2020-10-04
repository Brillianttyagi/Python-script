from tkinter import *
from math import *
import time

root = Tk()



def write(button):
	global eNum, bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9, bt0

	eNum.insert(END, int(button.cget('text')))


def add():
	global eNum

	eNum.insert(END, '+')

def sub():
	global eNum

	eNum.insert(END, '-')

def multi():
	global eNum

	eNum.insert(END, '*')

def div():
	global eNum

	eNum.insert(END, '/')


def equal():
	global eNum

	number = eNum.get()
	integers = eval(number)

	strint = integers
	eNum.destroy()
	eNum = Entry(root, width = 35)
	eNum.grid(row = 1, column = 0, columnspan = 5)
	eNum.insert(END, strint)





blank1 = Label(root, text = '')
blank1.grid(row = 0, column = 0)

eNum = Entry(root, width = 35)
eNum.grid(row = 1, column = 0, columnspan = 5)

bt1 = Button(root, text = '1', height = 5, width = 10, command = lambda: write(bt1))
bt1.grid(row = 4, column = 0)

bt2 = Button(root, text = '2', height = 5, width = 10, command = lambda: write(bt2))
bt2.grid(row = 4, column = 1)

bt3 = Button(root, text = '3', height = 5, width = 10, command = lambda: write(bt3))
bt3.grid(row = 4, column = 2)

bt4 = Button(root, text = '4', height = 5, width = 10, command = lambda: write(bt4))
bt4.grid(row = 3, column = 0)

bt5 = Button(root, text = '5', height = 5, width = 10, command = lambda: write(bt5))
bt5.grid(row = 3, column = 1)

bt6 = Button(root, text = '6', height = 5, width = 10, command = lambda: write(bt6))
bt6.grid(row = 3, column = 2)

bt7 = Button(root, text = '7', height = 5, width = 10, command = lambda: write(bt7))
bt7.grid(row = 2, column = 0)

bt8 = Button(root, text = '8', height = 5, width = 10, command = lambda: write(bt8))
bt8.grid(row = 2, column = 1)

bt9 = Button(root, text = '9', height = 5, width = 10, command = lambda: write(bt9))
bt9.grid(row = 2, column = 2)

bt0 = Button(root, text = '0', height = 5, width = 10, command = lambda: write(bt0))
bt0.grid(row = 5, column = 1)

btplus = Button(root, text = '+', height = 5, width = 10, command  = add)
btplus.grid(row = 5, column = 0)

btminus = Button(root, text = '-', height = 5, width = 10, command = sub)
btminus.grid(row = 5, column = 2)

btmulti = Button(root, text = '*', height = 5, width = 10, command = multi)
btmulti.grid(row = 6, column = 0)

btdiv = Button(root, text = '÷', height = 5, width = 10, command = div)
btdiv.grid(row = 6, column = 2)

btequal = Button(root, text = '=', height = 5, width = 10, command = equal)
btequal.grid(row = 6, column = 1)




mainloop()
