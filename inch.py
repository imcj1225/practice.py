from tkinter import *

window = Tk()
window.title("inch to cm")

cm = ""

def convert():
    cm = int(e1.get()) *2.54
    return

l1 = Label(window, text="인치입력")
l2 = Label(window, text = "입력: ")
e1 = Entry(window)
l3 = Label(window, text = "변환값: " + f'{cm}')
b1 = Button(window, text="변환", command = convert)

l1.grid(row = 0, columnspan=2)
l2.grid(row=1, column=0)
e1.grid(row=1, column=1)
l3.grid(row=2, columnspan=2)
b1.grid(row=3, columnspan=2)

window.mainloop()