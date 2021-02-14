from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('StringVar test')
root.geometry('300x200+100+100')
root.resizable(False, False)

def show():
    print(f'item1: {variety1.get()}')
    messagebox.showinfo('Button clicked', f'item1: {variety1.get()}')

variety1 = StringVar(value='영어') # '영어' 버튼이 선택된 상대로 표시됨

bt1 = Radiobutton(root, text='국어', value='국어', variable=variety1)
bt2 = Radiobutton(root, text='영어', value='영어', variable=variety1)
bt3 = Radiobutton(root, text='수학', value='수학', variable=variety1)
bt4 = Radiobutton(root, text='과학', value='과학', variable=variety1)

bt1.pack()
bt2.pack()
bt3.pack()
bt4.pack()

button = Button(root, width=10, text='Show', overrelief='solid', command=show)
button.pack()

root.mainloop()

