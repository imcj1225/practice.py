import tkinter

window=tkinter.Tk()
window.title("CHECKBUTTON")
window.geometry("300x200+100+100")
window.resizable(False,False)

def flash():
    checkbutton1.flash()

CheckVariety_1=tkinter.IntVar()
CheckVariety_2=tkinter.IntVar()

checkbutton1=tkinter.Checkbutton(window, text="check1", variable=CheckVariety_1)
checkbutton2=tkinter.Checkbutton(window, text="check2", variable=CheckVariety_2)
checkbutton3=tkinter.Checkbutton(window, text="check3", variable=CheckVariety_2)

checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()

window.mainloop()