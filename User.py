#!/usr/bin/python

import MySQLdb as mdb
import sys

class masterAccount:
	def __init__(self,username,password,idNum):
		self.username = username
		self.password = password
		self.idNum = idNum
	
	def createMasterAccount(self):
		con = mdb.connect('localhost','testuser','testAnnie','Fireproof');

		with con:
			cur = con.cursor()
			#cur.execute("DROP TABLE IF EXISTS FireproofAccountLogin")
			cur.execute("CREATE TABLE FireproofAccountLogin(Id INT PRIMARY KEY AUTO_INCREMENT, \
					 UserName VARCHAR(100), PasswordName VARCHAR(100))")
			cur.execute("INSERT INTO FireproofAccountLogin(UserName) VALUES (%s)", self.username)
			cur.execute("INSERT INTO FireproofAccountLogin(PasswordName) VALUES (%s)", self.password)


