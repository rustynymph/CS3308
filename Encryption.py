from Crypto.Cipher import AES
import hashlib
import base64
import os

class Encryption:

	@staticmethod
	def hashPassword(password):	return hashlib.sha256(password)

	@staticmethod
	def encryptCredentials(key,iv,text):
		encryption_suite = AES.new(key, AES.MODE_CFB, iv)
		return encryption_suite.encrypt(text)
	
	@staticmethod
	def decryptCredentials(key,iv,text):
		decryption_suite = AES.new(key, AES.MODE_CFB, iv)
		return decryption_suite.decrypt(text)