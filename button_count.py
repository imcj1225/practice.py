import tkinter
window = tkinter.Tk()
window.title("TEST")
window.geometry("650x400+100+100")
window.resizable(False, False)

count = 0

def countUP():
    global count
    count +=1
    label.config(text=str(count))

label = tkinter.Label(window, text = "0")
label.pack()

button = tkinter.Button(window, text = 'press', overrelief="solid", width = 15, command = countUP, repeatdelay = 1000, repeatinterval=100)
button.pack()

window.mainloop()