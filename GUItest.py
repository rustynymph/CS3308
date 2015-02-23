#!/usr/bin/python
#import Tkinter
from Tkinter import *
import tkMessageBox

window = Tk()
window.minsize(width=350, height=130)

userForm = Label(window,text="Username")
userForm.place(bordermode=OUTSIDE,x=10,y=10)

passForm = Label(window,text="Password")
passForm.place(bordermode=OUTSIDE,x=10,y=50)

userVar = Entry(window,bd=5)
userVar.place(bordermode=OUTSIDE,x=150,y=10)

username = userVar.get()

passVar = Entry(window,bd=5)
passVar.place(bordermode=OUTSIDE,x=150,y=50)

password = passVar.get()

def enterLoginInfo():
	if(not(username) or not(password)):
		tkMessageBox.showinfo("Error","Please enter username and password.")
	else:
		tkMessageBox.showinfo("Box","hey")

Enter = Button(window, text ="Enter", command = enterLoginInfo)

Enter.place(bordermode=OUTSIDE,x=120,y=100)
window.mainloop()
