#!/usr/bin/python

import MySQLdb as mdb
import sys
from config import *

class MasterAccount:
	def __init__(self,username,password,idNum):
		self.username = username
		self.password = password
		self.idNum = idNum
	
	#def encrypt(self):
	
	def insertMasterAccount(self):
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			cur.execute("DROP TABLE IF EXISTS FireproofAccountLogin")
			cur.execute("CREATE TABLE FireproofAccountLogin(Id INT PRIMARY KEY AUTO_INCREMENT, \
					 UserName VARCHAR(100), PasswordName VARCHAR(100))")
			cur.execute("INSERT INTO FireproofAccountLogin(UserName) VALUES (%s)", self.username)
			cur.execute("INSERT INTO FireproofAccountLogin(PasswordName) VALUES (%s)", self.password)
			
	def retrieveMasterAccount(self):
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()	

