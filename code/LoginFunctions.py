#!/usr/bin/python

import config
from MasterAccount import *
from FireproofProgram import *

class LoginFunctions:

	accounts = []

	@staticmethod
	def Login(master_username,master_password):
		if(not(master_username) or not(master_password)):
			tkMessageBox.showinfo("Error","Please enter username and password.")
			return False
		else:
			username_enc = None
			password_enc = None
			current_account = None
			for account in LoginFunctions.accounts:
				if (master_username == account.username) and (master_password == account.password):
					username_enc = account.username_enc
					password_enc = account.password_enc

					current_account = account

			if(not(MasterAccount.retrieveMasterAccountId(username_enc,password_enc))):
				tkMessageBox.showinfo("Create Login","Username and password not found. Please click create an account.")
				return False
			else: return current_account
			
	@staticmethod
	def createLoginInfo(master_username,master_password,confirm_master_password):
		username_characters = set(master_username)
		password_characters = set(master_password)
		if((not(master_username) or not(master_password)) or not(confirm_master_password)):
			tkMessageBox.showinfo("Error","Please enter required fields.")
		elif((' ' in username_characters) or (' ' in password_characters)):
			tkMessageBox.showinfo("Error","Usernames and passwords must not contain spaces.")
		elif(master_password != confirm_master_password):
			tkMessageBox.showinfo("Error","Passwords entered do not match.")
		elif(len(master_password) < 8):
			tkMessageBox.showinfo("Error","Password must be at least 8 characters.")
		else:
			account = MasterAccount(master_username,master_password)
			LoginFunctions.accounts += [account]
			MasterAccount.insertMasterAccount(account)

