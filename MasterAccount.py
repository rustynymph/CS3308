#!/usr/bin/python
#heart of our database

import MySQLdb as mdb
import sys
from config import *
import os
from Encryption import *

count = 0

class MasterAccount:
	def __init__(self,username,password):
		global count
		self.idNum = count
		count += 1
		self.username = username
		self.password = password
		key_hash_obj = Encryption.hashPassword(self.password) #sha256 more secure than md5
		#self.iv = os.urandom(16)
		self.iv = 'abcdefghijklmnop'
		self.key = key_hash_obj.digest()
		self.username_enc = Encryption.encryptCredentials(self.key,self.iv,self.username)
		self.password_enc = Encryption.encryptCredentials(self.key,self.iv,self.password)
				
	def insertMasterAccount(self):

		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			cur.execute("INSERT INTO FireproofAccountLogin (id,UserName,PasswordName) VALUES (%s,%s,%s)",(self.idNum,self.username_enc,self.password_enc))
			cur.execute("SELECT Id FROM FireproofAccountLogin WHERE (UserName,PasswordName) = (%s,%s)", (self.username_enc,self.password_enc))
			id_number = cur.fetchone()	
			self.idNum = id_number				
			
	def retrieveMasterAccount(self):
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()	
			cur.execute("SELECT Id FROM FireproofAccountLogin WHERE (UserName,PasswordName) = (%s,%s)", (self.username_enc,self.password_enc))
			id_number = cur.fetchone()
			
			if not(id_number):
				return None
			else:
				cur.execute("SELECT UserName FROM FireproofAccountLogin WHERE Id= %s",id_number)
				account_name = cur.fetchone()
				cur.execute("SELECT PasswordName FROM FireproofAccountLogin WHERE Id= %s",id_number)
				account_pass = cur.fetchone()
			
				if(account_name and account_pass):
					username = Encryption.decryptCredentials(self.key,self.iv,account_name[0])
					password = Encryption.decryptCredentials(self.key,self.iv,account_pass[0])
					print username
					print password
					print id_number
					return MasterAccount(username,password)
				else:
					return None


			
			

