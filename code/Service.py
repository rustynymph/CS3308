import MySQLdb as mdb
from config import *

class Service:
	
	ServiceCount = 1
	
	def __init__(self,service_name,service_accounts=[]):
		self.service_name = service_name
		self.service_accounts = service_accounts #will be a list of ServiceAccounts
		self.id_num = Service.ServiceCount
		Service.ServiceCount += 1

		self.service_name_enc = AESCipher.encryptCredentials(Fireproof.current_account.key,Fireproof.current_account.iv,self.service_name)
	
	@staticmethod
	def insertServiceName(account,service):

		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			insert_servicename_command = "INSERT INTO FireproofServices (id,masterid,ServiceName) VALUES (%s,%s,%s)"
			#cur.execute(insert_servicename_command,(self.id_num,service.service_name))
			cur.execute(insert_servicename_command,(service.id_num,account.id_num,service.service_name))

	@staticmethod
	def retrieveServiceName(account,service):
		account_id = account.id_nums

		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			retrieve_service_name_command = "SELECT id FROM FireproofServices WHERE (masterid,ServiceName) = (%s,%s)"
			cur.execute(retrieve_service_name_command,(account_id,service.service_name))
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


	
