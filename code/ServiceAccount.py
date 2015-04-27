import MySQLdb as mdb
from config import *
from AESCipher import *

class ServiceAccount:

	def __init__(self,username,password,account_owner):
		"""Constructor that initializes a ServiceAccount object

		:param username: username for the service
		:param password: password for the service
		:param account_owner: the master account for this service

		:return: A ServiceAccount object which stores the username and password for the service, the owner, and encrypted information
		"""

		self.username = username
		self.password = password
		self.account_owner = account_owner

		self.username_enc = AESCipher.encryptCredentials(self.account_owner.key,self.account_owner.iv,self.username)
		self.password_enc = AESCipher.encryptCredentials(self.account_owner.key,self.account_owner.iv,self.password)

	def __str__(self):
		return self.__class__.__name__ + "(" + self.username + ", " + self.password + ")"

	@staticmethod
	def insertServiceAccount(account,service,serviceaccount):
		"""Inserts the encrypted ServiceAccount into the database by matching it with the master account's and service account's primary id

		:param account: the master account who owns this service
		:param service: the service that this account is associated with
		"""		
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			insert_serviceaccount_command = "INSERT INTO FireproofServicesAccounts (serviceid,masterid,ServiceUsername,ServicePassword) VALUES (%s,%s,%s,%s)"
			#cur.execute(insert_servicename_command,(self.id_num,service.service_name))
			cur.execute(insert_serviceaccount_command,(service.id_num,account.id_num,serviceaccount.username_enc,serviceaccount.password_enc))


	@staticmethod
	def createServiceAccountsTable(): #createFireproofServicesAccountsTable
		"""Initializes the FireproofServicesAccounts table in our database"""
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			cur.execute("CREATE TABLE FireproofServicesAccounts (id INT(6) PRIMARY KEY AUTO_INCREMENT,serviceid INT(6),\
				masterid INT(6),ServiceUsername VARCHAR(30) NOT NULL,ServicePassword VARCHAR(30) NOT NULL)")	

	@staticmethod
	def removeServiceAccountFromDatabase(account,service):
		"""Deletes the specified Service from the database by matching its
		service id and master account's primary id
		
		:param account: The master account who owns this service
		"""
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);
		with con:
			cur = con.cursor()
			delete_service_command = "DELETE FROM FireproofServicesAccounts WHERE serviceid=%s AND masterid=%s"
			cur.execute(delete_service_command, (service.id_num, account.id_num))
	
	@staticmethod
	def changeServiceAccountUsername(account, service, new_username):
		"""Updates the specified service's stored username to be the newly provided username.
		
		:param account: The master account that owns this service
		"""
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);
		with con:
			cur = con.cursor()
			change_username_command= "UPDATE FireproofServicesAccounts SET ServiceUsername=%s WHERE id=%s AND serviceid=%s AND masterid=%s"
			cur.execute(change_username_command, (new_username, serviceaccount.id_num, service.id_num, account.id_num))
	
	@staticmethod
	def changeServicePassword(account, service, new_password):
		"""Updates the specified service's stored password to be the newly provided password.
		
		:param account: The master account that owns this service
		"""
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);
		with con:
			cur = con.cursor()
			change_password_command="UPDATE FireproofServices SET ServicePassword=%s WHERE id=%s AND serviceid=%s AND masterid=%s"
			cur.execute(change_password_command, (new_password, serviceaccount.id_num, service.id_num, account.id_num))
