from Service import *
from Encryption import *

class ServiceLogin:
	#serviceName is a string, logins is a dictionary
	#that way we can allow multiple accounts per service
	def __init__(self,serviceName,login):
		self.serviceName = serviceName
		self.login = login

	def insertServiceLogin(self):
		return 0

	def retrieveServiceLogin(self):
		return 0

	def editServiceLogin(self):
		return 0

	def removeServiceLogin(self):
		return 0