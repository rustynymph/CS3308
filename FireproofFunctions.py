#!/usr/bin/python
from Tkinter import *
import tkMessageBox
import config
from MasterAccount import *

class FireproofFunctions:

	@staticmethod
	def Login(MasterAccount):
		masterusername = MasterAccount.username
		masterpassword = MasterAccount.password
		masterid = MasterAccount.idNum
		if(not(masterusername) or not(masterpassword)):
			tkMessageBox.showinfo("Error","Please enter username and password.")
		else:
			account = MasterAccount
			if(not(MasterAccount.retrieveMasterAccount(account))):
				tkMessageBox.showinfo("Create Login","Username and password not found. Please create an account.")
				createLoginInfo()
			else:
				print account.username
				print account.password
				print account.idNum
			
	@staticmethod
	def createLoginInfo():
		masterusername = userVar.get()
		masterpassword = passVar.get()
		if(not(masterusername) or not(masterpassword)):
			tkMessageBox.showinfo("Error","Please enter username and password.")
		else:
			account = MasterAccount(masterusername,masterpassword,0)
			MasterAccount.insertMasterAccount(account)
			MasterAccount.retrieveMasterAccount(account)
