#!/usr/bin/python
from Tkinter import *
import tkMessageBox
import config
from MasterAccount import *
from FireproofFunctions import *
import MySQLdb as mdb
from config import *

class Page(Frame):
	def __init__(self, root):
		Frame.__init__(self, root)
	def show(self):
		self.lift()

class LoginPage(Page):
	def __init__(self, root):
		Frame.__init__(self, root)
		
		userForm = Label(root,text="Username")
		userForm.place(bordermode=OUTSIDE,x=60,y=140)

		passForm = Label(root,text="Password")
		passForm.place(bordermode=OUTSIDE,x=60,y=190)

		userVar = Entry(root,bd=5)
		userVar.place(bordermode=OUTSIDE,x=180,y=140)

		passVar = Entry(root,bd=5,show="*")
		passVar.place(bordermode=OUTSIDE,x=180,y=190)
		
		Enter = Button(root, text ="Login", command=lambda: FireproofFunctions.Login(userVar.get(),passVar.get()))
		Enter.place(bordermode=OUTSIDE,x=160,y=240)		
		
		Enter = Button(root, text ="Create Account", command=lambda: FireproofFunctions.createLoginInfo(userVar.get(),passVar.get()))
		Enter.place(bordermode=OUTSIDE,x=235,y=240)	

class CreateAccountPage(Page):
	def __init__(self, root):
		Frame.__init__(self, root)
		
		userForm = Label(root,text="Create Username")
		userForm.place(bordermode=OUTSIDE,x=60,y=140)

		passForm = Label(root,text="Create Password")
		passForm.place(bordermode=OUTSIDE,x=60,y=190)

		userVar = Entry(root,bd=5)
		userVar.place(bordermode=OUTSIDE,x=180,y=140)

		passVar = Entry(root,bd=5,show="*")
		passVar.place(bordermode=OUTSIDE,x=180,y=190)
		
		Enter = Button(root, text ="Create Account", command=lambda: FireproofFunctions.createLoginInfo(userVar.get(),passVar.get()))
		Enter.place(bordermode=OUTSIDE,x=292,y=240)
			

class RetrieveAccounts(Page):
	def __init__(self, root):
		Frame.__init__(self, root)
		label = Label(self, text="This is page 3")
		label.pack(side="top", fill="both", expand=True)	

class FirstView(Frame):
	def __init__(self, root):
		Frame.__init__(self, root)
		self.root = root
		self.page = 0
		p1 = LoginPage(self)

		logo = PhotoImage(file="fireproof.png")
		w1 = Label(image=logo)
		w1.image = logo
		w1.place(bordermode=OUTSIDE,x=85,y=25)

		p1.lift()


if __name__ == "__main__":
	con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);
	with con:
		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS FireproofAccountLogin")
		cur.execute("CREATE TABLE FireproofAccountLogin(Id INT NOT NULL AUTO_INCREMENT,UserName VARCHAR(512), PasswordName VARCHAR(512),PRIMARY KEY (id))")
	root = Tk()
	main = FirstView(root)
	main.pack(side="top", fill="both", expand=True)
	root.wm_geometry("400x300")
	root.mainloop()
