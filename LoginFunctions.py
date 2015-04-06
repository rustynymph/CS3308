#!/usr/bin/python
from Tkinter import *
import tkMessageBox
import config
from MasterAccount import *
#from GUIpages import *
from FireproofProgram import *

class LoginFunctions:

	accounts = []

	@staticmethod
	def Login(masterusername,masterpassword):
		if(not(masterusername) or not(masterpassword)):
			tkMessageBox.showinfo("Error","Please enter username and password.")
			return False
		else:
			loginAccount = None
			for account in LoginFunctions.accounts:
				if (masterusername == account.username) and (masterpassword == account.password):
					loginAccount = account
			#account = MasterAccount(masterusername,masterpassword)
			if(not(MasterAccount.retrieveMasterAccount(loginAccount))):
				tkMessageBox.showinfo("Create Login","Username and password not found. Please click create an account.")
				return False
				
			else:
				#print account.username
				#print account.password
				#print account.idNum
				return True
			
	@staticmethod
	def createLoginInfo(masterusername,masterpassword,confirmmasterpassword):
		if((not(masterusername) or not(masterpassword)) or not(confirmmasterpassword)):
			tkMessageBox.showinfo("Error","Please enter required fields.")
		elif(masterpassword != confirmmasterpassword):
			tkMessageBox.showinfo("Error","Passwords entered do not match.")
		else:
			if(len(masterpassword) < 8):
				tkMessageBox.showinfo("Error","Password must be at least 8 characters.")
			#elif:
			#elif:
			else:
				account = MasterAccount(masterusername,masterpassword)
				LoginFunctions.accounts += [account]
				MasterAccount.insertMasterAccount(account)

