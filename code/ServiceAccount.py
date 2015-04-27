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

			get_serviceaccountid_command = "SELECT id FROM FireproofServicesAccounts WHERE ServiceUsername=%s AND ServicePassword=%s"
			cur.execute(get_serviceaccountid_command,(serviceaccount.username_enc,serviceaccount.password_enc))
			serviceaccount.id_num = cur.fetchone()


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
	