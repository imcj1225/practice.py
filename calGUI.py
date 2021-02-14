from tkinter import *

calc = Tk()
calc.title("Calculator")
calc.geometry("300x300")

#def enter(event):
#    result = eval(display.get())
#    print(result)
#    display.delete(0,END)
#    display.insert(0,result)

def button_pressed(value):
    display.insert(END,value)
    print(value,'pressed')

def calculate():
    result = eval(display.get())
    print(result)
    display.delete(0,END)
    display.insert(0,result)

def empty():
    display.delete(0,END)

display = Entry(calc, width= 20)

b0 = Button(calc, text='0', command=lambda:button_pressed('0'))
b1 = Button(calc, text='1', command=lambda:button_pressed('1'))
b2 = Button(calc, text='2', command=lambda:button_pressed('2'))
b3 = Button(calc, text='3', command=lambda:button_pressed('3'))
b4 = Button(calc, text='4', command=lambda:button_pressed('4'))
b5 = Button(calc, text='5', command=lambda:button_pressed('5'))
b6 = Button(calc, text='6', command=lambda:button_pressed('6'))
b7 = Button(calc, text='7', command=lambda:button_pressed('7'))
b8 = Button(calc, text='8', command=lambda:button_pressed('8'))
b9 = Button(calc, text='9', command=lambda:button_pressed('9'))

b_plus = Button(calc, text='+', command=lambda:button_pressed('+'))
b_minus = Button(calc, text='-', command=lambda:button_pressed('-'))
b_mul = Button(calc, text='*', command=lambda:button_pressed('*'))
b_div = Button(calc, text='/', command=lambda:button_pressed('/'))
b_equal = Button(calc, text='=', command=calculate)
b_ac = Button(calc, text='AC', command=empty)

display.grid(row=0, columnspan=4)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b_div.grid(row=1, column=3)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b_mul.grid(row=2, column=3)
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b_plus.grid(row=3, column=3)
b_ac.grid(row=4, column=0)
b0.grid(row=4, column=1)
b_equal.grid(row=4, column=2)
b_minus.grid(row=4,column=3)


calc.mainloop()