import tkinter

window=tkinter.Tk()
window.title("HELLO")
window.geometry("300x200+100+100")
window.resizable(False, False)

def calc(event):
    label.config(text="결과="+str(entry.get()))

entry = tkinter.Entry(window)
entry.bind("<Return>", calc)
entry.pack()

label=tkinter.Label(window)
label.pack()

window.mainloop()