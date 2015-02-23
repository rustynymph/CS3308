#!/usr/bin/python
#heart of our database

import MySQLdb as mdb
import sys
from config import *
from Crypto.Cipher import AES
import hashlib
import base64
import os

class MasterAccount:
	def __init__(self,username,password,idNum):
		self.username = username
		self.password = password
		self.idNum = idNum
		
		key_hash_obj = hashlib.md5(self.password)
		self.key = key_hash_obj.digest()
		
		self.iv = os.urandom(16)
	
	@staticmethod
	def encryptCredentials(key,iv,text):
		encryption_suite = AES.new(key, AES.MODE_CFB, iv)
		return encryption_suite.encrypt(text)
	
	@staticmethod
	def decryptCredentials(key,iv,text):
		decryption_suite = AES.new(key, AES.MODE_CFB, iv)
		return decryption_suite.decrypt(text)
		
	def insertMasterAccount(self):
		username_enc = MasterAccount.encryptCredentials(self.key,self.iv,self.username)
		password_enc = MasterAccount.encryptCredentials(self.key,self.iv,self.password)	
				
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			cur.execute("DROP TABLE IF EXISTS FireproofAccountLogin")
			cur.execute("CREATE TABLE FireproofAccountLogin(Id INT,UserName VARCHAR(512), PasswordName VARCHAR(512))")
			cur.execute("INSERT INTO FireproofAccountLogin (Id,UserName,PasswordName) VALUES (%s,%s,%s)",(self.idNum,username_enc, password_enc))
			
	def retrieveMasterAccount(self):
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()	
			cur.execute("SELECT UserName FROM FireproofAccountLogin WHERE Id=0")
			account_name = cur.fetchone()
			cur.execute("SELECT PasswordName FROM FireproofAccountLogin WHERE Id=0")
			account_pass = cur.fetchone()
			
			if(account_name and account_pass):
				username = MasterAccount.decryptCredentials(self.key,self.iv,account_name[0])
				password = MasterAccount.decryptCredentials(self.key,self.iv,account_pass[0])
				return MasterAccount(username,password,0)
			else:
				return None


			
			

