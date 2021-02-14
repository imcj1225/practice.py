from tkinter import*
root = Tk()
root.title('hello')
root.geometry('300x200+100+100')
root.resizable(False, False)

label = Label(root, text = 'Hello World!', width=10, height=10, fg='red')
label.pack()

button = Button(root, width=20, height=10, text='push')
button.pack()

root.mainloop()

