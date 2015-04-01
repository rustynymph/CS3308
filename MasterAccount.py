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
	def __init__(self,username,password):
		self.username = username
		self.password = password
		#self.idNum = idNum
		#key_hash_obj = hashlib.md5(self.password)
		key_hash_obj = hashlib.sha256(self.password)
		#self.iv = os.urandom(16)
		self.iv = 'abcdefghijklmnop'
		self.key = key_hash_obj.digest()
		self.username_enc = MasterAccount.encryptCredentials(self.key,self.iv,self.username)
		self.password_enc = MasterAccount.encryptCredentials(self.key,self.iv,self.password)
	
	@staticmethod
	def encryptCredentials(key,iv,text):
		encryption_suite = AES.new(key, AES.MODE_CFB, iv)
		return encryption_suite.encrypt(text)
	
	@staticmethod
	def decryptCredentials(key,iv,text):
		decryption_suite = AES.new(key, AES.MODE_CFB, iv)
		return decryption_suite.decrypt(text)
			
	def insertMasterAccount(self):
			
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			cur.execute("DROP TABLE IF EXISTS FireproofAccountLogin")
			cur.execute("CREATE TABLE FireproofAccountLogin (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,UserName VARCHAR(30) NOT NULL,\
				PasswordName VARCHAR(30) NOT NULL)")

			cur.execute("INSERT INTO FireproofAccountLogin (UserName,PasswordName) VALUES (%s,%s)",(self.username_enc,self.password_enc))
			#cur.execute("SELECT Id FROM FireproofAccountLogin WHERE (UserName,PasswordName) = (%s,%s)", (self.username_enc,self.password_enc))
			#id_number = cur.fetchone()			
			#cur.execute("CREATE TABLE %s", (id_number))
		
			
	def retrieveMasterAccount(self):
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()	
			#cur.execute("SELECT UserName FROM FireproofAccountLogin WHERE Id=0")
			#account = cur.fetchone()
			#print str(account[0]) == str(self.username_enc)
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
					username = MasterAccount.decryptCredentials(self.key,self.iv,account_name[0])
					password = MasterAccount.decryptCredentials(self.key,self.iv,account_pass[0])
					print username
					print password
					print id_number
					return MasterAccount(username,password)
				else:
					return None


			
			

