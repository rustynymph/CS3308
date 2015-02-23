#!/usr/bin/python
#import Tkinter
from Tkinter import *
import tkMessageBox
import config
from MasterAccount import *
from GUIpages import *


con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS FireproofAccountLogin")
	cur.execute("CREATE TABLE FireproofAccountLogin(Id INT,UserName VARCHAR(512), PasswordName VARCHAR(512))")

window = Tk()
window.minsize(width=350, height=100)

#Page.show(LoginPage)

userForm = Label(window,text="Username")
userForm.place(bordermode=OUTSIDE,x=10,y=10)

passForm = Label(window,text="Password")
passForm.place(bordermode=OUTSIDE,x=10,y=50)

userVar = Entry(window,bd=5)
userVar.place(bordermode=OUTSIDE,x=150,y=10)

passVar = Entry(window,bd=5,show="*")
passVar.place(bordermode=OUTSIDE,x=150,y=50)

def Login():
	masterusername = userVar.get()
	masterpassword = passVar.get()
	if(not(masterusername) or not(masterpassword)):
		tkMessageBox.showinfo("Error","Please enter username and password.")
	else:
		account = MasterAccount(masterusername,masterpassword,0)
		if(not(MasterAccount.retrieveMasterAccount(account))):
			tkMessageBox.showinfo("Create Login","Username and password not found. Please create an account.")
			createLoginInfo()
		else:
			print account.username
			print account.password
			print account.idNum
		
#edit 
def createLoginInfo():
	masterusername = userVar.get()
	masterpassword = passVar.get()
	if(not(masterusername) or not(masterpassword)):
		tkMessageBox.showinfo("Error","Please enter username and password.")
	else:
		account = MasterAccount(masterusername,masterpassword,0)
		MasterAccount.insertMasterAccount(account)
		MasterAccount.retrieveMasterAccount(account)

#Enter = Button(window, text ="Enter", command = createLoginInfo)
Enter = Button(window, text ="Enter", command = Login)

Enter.place(bordermode=OUTSIDE,x=120,y=100)
window.mainloop()
