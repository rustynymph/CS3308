import MySQLdb as mdb
from config import *
from AESCipher import *
from FireproofProgram import *

class Service:
	
	ServiceCount = 1
	
	def __init__(self,service_name,account_owner,service_accounts=[]):
		self.service_name = service_name
		self.account_owner = account_owner
		self.service_accounts = service_accounts #will be a list of ServiceAccounts
		self.id_num = Service.ServiceCount
		Service.ServiceCount += 1

		self.service_name_enc = AESCipher.encryptCredentials(self.account_owner.key,self.account_owner.iv,self.service_name)

	def __str__(self):
		return self.__class__.__name__ + "(" + self.service_name + ", " + self.service_accounts + ")"
	
	@staticmethod
	def insertServiceName(account,service):

		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			insert_servicename_command = "INSERT INTO FireproofServices (id,masterid,ServiceName) VALUES (%s,%s,%s)"
			#cur.execute(insert_servicename_command,(self.id_num,service.service_name))
			cur.execute(insert_servicename_command,(service.id_num,account.id_num,service.service_name_enc))

	@staticmethod
	def retrieveServiceNameId(account,service):
		service_name_enc = service.service_name_enc

		account_id = account.id_nums

		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			retrieve_service_name_command = "SELECT id FROM FireproofServices WHERE (masterid,ServiceName) = (%s,%s)"
			cur.execute(retrieve_service_name_command,(account_id,service_name_enc))
			service_primary_key = cur.fetchone()
			print service_primary_key		

	@staticmethod
	def changeService(account,service):
		
		account_id = account.id_num	

		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			retrieve_service_name_command = "SELECT id FROM FireproofServices WHERE (masterid,ServiceName) = (%s,%s)"
			cur.execute(retrieve_service_name_command,(account_id,service.service_name))
			service_primary_key = cur.fetchone()
			print service_primary_key			

	@staticmethod
	def createServiceTable():
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			cur.execute("DROP TABLE IF EXISTS FireproofServices")
			cur.execute("CREATE TABLE FireproofServices (id INT(6) PRIMARY KEY,masterid INT(6),ServiceName VARCHAR(30) NOT NULL)")


	
