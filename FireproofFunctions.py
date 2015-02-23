#!/usr/bin/python
from Tkinter import *
import tkMessageBox
import config
from MasterAccount import *
from GUIpages import *

class FireproofFunctions:

	@staticmethod
	def Login(masterusername,masterpassword):
		if(not(masterusername) or not(masterpassword)):
			tkMessageBox.showinfo("Error","Please enter username and password.")
		else:
			account = MasterAccount(masterusername,masterpassword,0)
			if(not(MasterAccount.retrieveMasterAccount(account))):
				tkMessageBox.showinfo("Create Login","Username and password not found. Please click create an account.")
				
			else:
				print account.username
				print account.password
				print account.idNum
			
	@staticmethod
	def createLoginInfo(masterusername,masterpassword):
		if(not(masterusername) or not(masterpassword)):
			tkMessageBox.showinfo("Error","Please enter username and password.")
		else:
			account = MasterAccount(masterusername,masterpassword,0)
			MasterAccount.insertMasterAccount(account)

