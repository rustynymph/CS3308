import MySQLdb as mdb
from config import *

class ServiceAccount:

	def __init__(self,username,password):
		self.username = username
		self.password = password

		#self.username_enc
		#self.password_enc

	@staticmethod
	def insertServiceAccount(account,service,serviceaccount):
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			insert_serviceaccount_command = "INSERT INTO FireproofServicesAccounts (serviceid,masterid,ServiceUsername,ServicePassword) VALUES (%s,%s,%s,%s)"
			#cur.execute(insert_servicename_command,(self.id_num,service.service_name))
			cur.execute(insert_serviceaccount_command,(service.id_num,account.id_num,serviceaccount.username,serviceaccount.password))


	@staticmethod
	def createServiceAccountsTable():
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			cur.execute("CREATE TABLE FireproofServicesAccounts (id INT(6) PRIMARY KEY AUTO_INCREMENT,serviceid INT(6),\
				masterid INT(6),ServiceUsername VARCHAR(30) NOT NULL,ServicePassword VARCHAR(30) NOT NULL)")	
