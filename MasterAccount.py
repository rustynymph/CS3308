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
		self.id_num = count
		count += 1
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
			cur.execute("INSERT INTO FireproofAccountLogin (id,UserName,PasswordName) VALUES (%s,%s,%s)",(self.id_num,self.username_enc,self.password_enc))
			cur.execute("SELECT Id FROM FireproofAccountLogin WHERE (UserName,PasswordName) = (%s,%s)", (self.username_enc,self.password_enc))
			id_number = cur.fetchone()	
			self.id_num = id_number				
	
	@staticmethod		
	def retrieveMasterAccount(account):
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()	
			cur.execute("SELECT Id FROM FireproofAccountLogin WHERE (UserName,PasswordName) = (%s,%s)", (account.username_enc,account.password_enc))
			id_number = cur.fetchone()
		
		return id_number


			
			

