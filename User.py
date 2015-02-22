#!/usr/bin/python

import MySQLdb as mdb
import sys
from config import *
from Crypto.Cipher import AES
import hashlib
import base64

class MasterAccount:
	def __init__(self,username,password,idNum):
		self.username = username
		self.password = password
		self.idNum = idNum
	
	@staticmethod
	def encryptCredentials(key,text):
		text_hash_obj = hashlib.md5(text)
		new_text = text_hash_obj.digest()
		iv = 'This is an IV456'
		encryption_suite = AES.new(key, AES.MODE_CBC, iv)
		return encryption_suite.encrypt(new_text)
	
	def insertMasterAccount(self):
		key_hash_obj = hashlib.md5(self.password)
		key = key_hash_obj.digest()
		
		username_enc = MasterAccount.encryptCredentials(key,self.username)
		password_enc = MasterAccount.encryptCredentials(key,self.password)
				
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			cur.execute("DROP TABLE IF EXISTS FireproofAccountLogin")
			cur.execute("CREATE TABLE FireproofAccountLogin(Id INT PRIMARY KEY AUTO_INCREMENT, \
					 UserName VARCHAR(100), PasswordName VARCHAR(100))")
			cur.execute("INSERT INTO FireproofAccountLogin(UserName) VALUES (%s)", username_enc)
			cur.execute("INSERT INTO FireproofAccountLogin(PasswordName) VALUES (%s)", password_enc)
			
	def retrieveMasterAccount(self):
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()	
			cur.execute("SELECT * FROM FireproofAccountLogin")
			accounts = cur.fetchall()
			for row in accounts:
				print row

