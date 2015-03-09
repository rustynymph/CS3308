#!/usr/bin/python
from Tkinter import *
import tkMessageBox
import config
from MasterAccount import *
#from GUIpages import *
from FireproofProgram import *

class FireproofFunctions:

	@staticmethod
	def Login(masterusername,masterpassword,page,frames):
		if(not(masterusername) or not(masterpassword)):
			tkMessageBox.showinfo("Error","Please enter username and password.")
		else:
			account = MasterAccount(masterusername,masterpassword,0)
			if(not(MasterAccount.retrieveMasterAccount(account))):
				tkMessageBox.showinfo("Create Login","Username and password not found. Please click create an account.")
				
			else:
				#PageName = page.__name__
				#SPage = self.page
				#PageName.tkraise()
				print page
				print frames
				Fireproof.show_frame(page.__name__)
				print account.username
				print account.password
				print account.idNum
				return True
			
	@staticmethod
	def createLoginInfo(masterusername,masterpassword,confirmmasterpassword):
		if((not(masterusername) or not(masterpassword)) or not(confirmmasterpassword)):
			tkMessageBox.showinfo("Error","Please enter required fields.")
		elif(masterpassword != confirmmasterpassword):
			tkMessageBox.showinfo("Error","Passwords entered do not match.")
		else:
			account = MasterAccount(masterusername,masterpassword,0)
			MasterAccount.insertMasterAccount(account)

