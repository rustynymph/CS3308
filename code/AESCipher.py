from Crypto.Cipher import AES
import hashlib
import os

BLOCKSIZE = 16

class AESCipher:

	#in order to use AES in CBC mode we must pad our input using PKCS5
	#so that our string is a multiple of 16 bytes

	#PKCS5 padding algorithm
	pad = staticmethod(lambda text: text + (BLOCKSIZE - len(text) % BLOCKSIZE) * chr(BLOCKSIZE - len(text) % BLOCKSIZE))
	"""Takes a string of text as input and pads it to make its length a multiple of 16"""

	unpad = staticmethod(lambda text : text[0:-ord(text[-1])])
	"""Takes padded text as input and strips the extra padding from it"""

	@staticmethod
	def hashPassword(password):
		""" Hashes the given password string using sha256.

		:param password: a string of at least 8 characters
		:return: returns a hash of 256 bits

		"""
		return hashlib.sha256(password)

	@staticmethod
	def encryptCredentials(key,iv,text):
		""" Creates an AES128 encryption suite that includes a symmetric key and an initialization vector (iv).
		The key is created by hashing the master password using sha256 and the iv is created using
		os.random(16). Using the encryption suite we can encrypt the given string of text.

        :param key: symmetric key used in the AES128 suite
        :param iv: random 16 bit iv used in the AES128 suite
        :param text: a string of text
        :return: returns an encrypted string of text that is a multiple of 16 bits

		"""
		padded_text = AESCipher.pad(text)
		encryption_suite = AES.new(key, AES.MODE_CBC, iv)
		return encryption_suite.encrypt(padded_text)
	
	@staticmethod
	def decryptCredentials(key,iv,text):
		""" Creates an AES128 decryption suite that includes the symmetric key and iv for the particular master
		account.  We use the decryption suite to decrypt the given string of text.

        :param key: symmetric key used in the AES128 suite
        :param iv: random 16 bit iv used in the AES128 suite
        :param text: an encrypted string that is a multiple of 16 bits
        :return: returns the decrypted text

		"""
		decryption_suite = AES.new(key, AES.MODE_CBC, iv)
		decrypted_padded_text = decryption_suite.decrypt(text)
		return AESCipher.unpad(decrypted_padded_text)