#!/usr/bin/python

import config
from MasterAccount import *

#confusion with the naming in createLoginInfo and createAccount -> names should be more differentiated for clarity?

class LoginFunctions:

	accounts = []

	@staticmethod
	def Login(master_username,master_password): #checkLogin
		"""Checks a user's Username and Password against the master account database. The user enters his/her credentials 
		which are checked against the database to see if a matching Username & Password combination exist. If a username or 
		password is not provided, an error message appears asking the user to enter one. If the credentials don't match any
		existing master accounts in the database, an error message asks the user to create an account, otherwise the user 
		successfully logs into their Fireproof account. 
		
		:param master_username: the main username used to login to Fireproof (checked against database)
		:param master_password: the main password used to login to Fireproof (checked against database)
		:return: returns the current account based on the username and password provided by the user. 
		
		"""
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
		"""Creates a new master account in the database when a new user signs up for Fireproof. The Master Username and Password
		then uses the insertMasterAccount function to be inserted as a new set in the database of master account. Error messages handle
		malformed inputs for either username, password, or confirm password. Upon successful input of credentials, a new master account is
		created and the user returns to the Login function. 
		
		:param master_username: the main username used to login to Fireproof (checked against database)
		:param master_password: the main password used to login to Fireproof (checked against database)
		
		"""
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


	@staticmethod
	def checkIfUser(username,password,frame,controller):
		""" This function checks to see if the inputted information exists
		in the database, and if so, displays the next page. Otherwise,
		it returns an error to the user.
		"""
		is_a_user = LoginFunctions.Login(username,password)
		if is_a_user:
			print is_a_user
			controller.current_account = is_a_user
			frame.username_input_form.delete(0, 'end')
			frame.password_input_form.delete(0, 'end')
			controller.show_frame(controller.ServicesPage)


	@staticmethod
	def createAccount(username,password,confirm_password,frame,controller):
		""" This creates the user account when the create account 
		button is selected. It also clears the information from the 
		fields, and then displays the login page for the user.
		"""
		LoginFunctions.createLoginInfo(username,password,confirm_password)
		frame.username_input_form.delete(0, 'end')
		frame.password_input_form.delete(0, 'end')
		frame.confirm_password_input_form.delete(0, 'end')
		controller.show_frame(controller.LoginPage)			
