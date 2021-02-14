from tkinter import *
def keyPressed(event):
    print(event.char)
root = Tk()
frame = Frame(root, width=100, height=100)

frame.bind('<Key>', keyPressed)
frame.place(x=0, y=0)
frame.focus_set()
root.mainloop()

