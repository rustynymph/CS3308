#!/usr/bin/python
from Tkinter import *
import tkMessageBox
import config
from MasterAccount import *
from FireproofFunctions import *

class Page(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
	def show(self):
		self.lift()

class LoginPage(Page):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
		label = Label(self, text="This is page 1")
		label.pack(side="top", fill="both", expand=True)
		
		userForm = Label(root,text="Username")
		userForm.place(bordermode=OUTSIDE,x=60,y=140)

		passForm = Label(root,text="Password")
		passForm.place(bordermode=OUTSIDE,x=60,y=190)

		userVar = Entry(root,bd=5)
		userVar.place(bordermode=OUTSIDE,x=180,y=140)

		passVar = Entry(root,bd=5,show="*")
		passVar.place(bordermode=OUTSIDE,x=180,y=190)
		
		account_info = MasterAccount(userVar.get(),passVar.get(),0)
		
		Enter = Button(root, text ="Enter", command = FireproofFunctions.Login(account_info))
		Enter.place(bordermode=OUTSIDE,x=292,y=240)		

class CreateAccountPage(Page):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
		label1 = Label(self, text="This is page 2")
		label1.pack(side="top", fill="both", expand=True)

class RetrieveAccounts(Page):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
		label = Label(self, text="This is page 3")
		label.pack(side="top", fill="both", expand=True)	

class StorageView(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
		p1 = LoginPage(self)
		p2 = CreateAccountPage(self)
		p3 = RetrieveAccounts(self)

		buttonframe = Frame(self)
		container = Frame(self)
		buttonframe.pack(side="top", fill="x", expand=False)
		container.pack(side="top", fill="both", expand=True)

		p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

		b1 = Button(buttonframe, text="Page 1", command=lambda: p1.lift())
		b2 = Button(buttonframe, text="Page 2", command=lambda: p2.lift())
		b3 = Button(buttonframe, text="Page 3", command=lambda: p3.lift())

		b1.pack(side="left")
		b2.pack(side="left")
		b3.pack(side="left")

		p1.show()
		
class MainView(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
		p1 = LoginPage(self)

		logo = PhotoImage(file="fireproof.png")
		w1 = Label(image=logo)
		w1.image = logo
		w1.place(bordermode=OUTSIDE,x=85,y=25)

		#buttonframe = Frame(self)
		#container = Frame(self)
		#buttonframe.pack(side="top", fill="x", expand=False)
		#container.pack(side="top", fill="both", expand=True)

		p1.lift()


if __name__ == "__main__":
	root = Tk()
	main = MainView(root)
	main.pack(side="top", fill="both", expand=True)
	root.wm_geometry("400x300")
	root.mainloop()
