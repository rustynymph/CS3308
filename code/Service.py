class Service:

	def __init__(self,service_name,service_accounts):
		self.service_name = service_name
		self.service_accounts = service_accounts #will be a list of ServiceAccounts

		#self.service_name_enc = 

class ServiceAccount:

	def __init__(self,username,password):
		self.username = username
		self.password = password

		#self.username_enc
		#self.password_enc