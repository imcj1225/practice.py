from tkinter import *

window = Tk()
window.title("Login")

user_id = StringVar()
user_pw = StringVar()

def check_data():
    if user_id.get() == 'hello' and user_pw.get() == '1234':
        print('login complete')
    else:
        print('ID/PW not correct!')

id = Label(window, text="ID: ")
box1 = Entry(window, textvariable=user_id)
pw = Label(window, text="PW: ")
box2 = Entry(window, textvariable=user_pw)
login = Button(window, text="Login", command=check_data)

id.grid(row=0, column=0)
box1.grid(row=0, column=1)
pw.grid(row=1, column=0)
box2.grid(row=1, column=1)
login.grid(row=2, columnspan=2)

window.mainloop()