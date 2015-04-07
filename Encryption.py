from Crypto.Cipher import AES
import hashlib
import base64
import os

BLOCKSIZE = 16

class Encryption:

	#in order to use AES in CBC mode we must pad our input using PKCS5
	#so that our string is a multiple of 16 bytes

	#PKCS5 padding algorithm
	pad = staticmethod(lambda text: text + (BLOCKSIZE - len(text) % BLOCKSIZE) * chr(BLOCKSIZE - len(text) % BLOCKSIZE))
	unpad = staticmethod(lambda text : text[0:-ord(text[-1])])

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