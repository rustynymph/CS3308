from MasterAccount import *
from Encryption import *

class MainService:
	#serviceName is a string, logins is a dictionary
	#that way we can allow multiple accounts per service
	def __init__(self,serviceName,logins):
		self.serviceName = serviceName
		self.logins = logins

	def insertService(self):
		return 0

	def retrieveService(self):
		return 0

	def editService(self):
		return 0

	def removeService(self):
		return 0