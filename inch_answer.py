from tkinter import *

window = Tk()
window.title('inch to cm')

def convert():
    result = float(e1.get()) *2.54
    l4.config(text=f'{result} cm')

l1 = Label(window, text = "인치변환프로그램")
l1.grid(row = 0, columnspan = 2)
l2 = Label(window, text = "입력: ")
l2.grid(row=1, column=0)
e1 = Entry(window)
e1.grid(row=1, column=1)
l3 = Label(window, text = "변환값")
l3.grid(row=2, column=0)
l4 = Label(window, text = "")
l4.grid(row=2, column=1)
b1 = Button(window, text = "변환", command = convert)
b1.grid(row=3, columnspan=2)

window.mainloop()