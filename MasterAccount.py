#!/usr/bin/python
#heart of our database

import MySQLdb as mdb
import sys
from config import *
import os
from Encryption import *

class MasterAccount:

	count = 0

	def __init__(self,username,password):
		self.id_num = MasterAccount.count
		MasterAccount.count += 1
		self.username = username
		self.password = password
		key_hash_obj = Encryption.hashPassword(self.password) #sha256 more secure than md5
		self.iv = os.urandom(16)
		self.key = key_hash_obj.digest()
		self.username_enc = Encryption.encryptCredentials(self.key,self.iv,self.username)
		self.password_enc = Encryption.encryptCredentials(self.key,self.iv,self.password)
				
	def insertMasterAccount(self):

		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			#important info on preventing SQL injection
			#http://bobby-tables.com/python.html
			
			insert_account_command = "INSERT INTO FireproofAccountLogin (id,UserName,PasswordName) VALUES (%s,%s,%s)"
			cur.execute(insert_account_command,(self.id_num,self.username_enc,self.password_enc))
	
	@staticmethod		
	def retrieveMasterAccount(account):
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			retrieve_account_id_command = "SELECT Id FROM FireproofAccountLogin WHERE (UserName,PasswordName) = (%s,%s)"
			cur.execute(retrieve_account_id_command, (account.username_enc,account.password_enc))
			id_number = cur.fetchone()

		return id_number


			
			

