from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('check message')
root.geometry('300x200+100+100')
root.resizable(False, False)

def show():
    print(f'item1: {var1.get()}, item2: {var2.get()}, item3: {var3.get()}')
    messagebox.showinfo("Button clicked!", f'item1: {var1.get()}, item2: {var2.get()}, item3: {var3.get()}')

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

bt1 = Checkbutton(root, text='item1', variable=var1)
bt2 = Checkbutton(root, text='item2', variable=var2)
bt3 = Checkbutton(root, text='item3', variable=var3)

bt1.pack()
bt2.pack()
bt3.pack()

button = Button(root, width=10, text='Show', overrelief='solid', command=show)
button.pack()

root.mainloop()