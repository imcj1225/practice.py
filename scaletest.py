from tkinter import *

root = Tk()
root.title('SCALE TEST')
root.geometry('300x200+100+100')
root.resizable(False, False)

def select(event):
    value = f'값: {str(scale.get())}'
    label.config(text = value)

var1 = IntVar()

scale = Scale(root, variable=var1, orient='horizontal', showvalue=True, tickinterval=10, to=100, length=100, command=select)
scale.pack()

label = Label(root, text='0')
label.pack()

root.mainloop()