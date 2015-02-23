#!/usr/bin/python
from Tkinter import *
import tkMessageBox
import config
from MasterAccount import *

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

class CreateAccountPage(Page):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
		label = Label(self, text="This is page 2")
		label.pack(side="top", fill="both", expand=True)

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

	

if __name__ == "__main__":
	root = Tk()
	main = MainView(root)
	main.pack(side="top", fill="both", expand=True)
	root.wm_geometry("400x400")
	root.mainloop()
