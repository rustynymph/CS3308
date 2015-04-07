from Crypto.Cipher import AES
import hashlib
import base64
import os

#BS = 16
#pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
#unpad = lambda s : s[0:-ord(s[-1])]

class Encryption:

	#in order to use AES in CBC mode we must pad our input using PKCS5
	#so that our string is a multiple of 16 bytes

	#PKCS5 padding algorithm
	@staticmethod
	def pad(text): return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)

	#PKCS5 unpadding algorithm
	@staticmethod
	def unpad(text): return text[0:-ord(text[-1])]

	@staticmethod
	def hashPassword(password):	return hashlib.sha256(password)

	@staticmethod
	def encryptCredentials(key,iv,text):
		padded_text = Encryption.pad(text)
		encryption_suite = AES.new(key, AES.MODE_CBC, iv)
		return encryption_suite.encrypt(padded_text)
	
	@staticmethod
	def decryptCredentials(key,iv,text):
		decryption_suite = AES.new(key, AES.MODE_CBC, iv)
		decrypted_padded_text = decryption_suite.decrypt(text)
		return Encryption.unpad(decrypted_padded_text)