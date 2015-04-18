class Service:

	def __init__(self,service_name,service_accounts):
		self.service_name = service_name
		self.service_accounts = service_accounts #will be a list of ServiceAccounts

		#self.service_name_enc = 

	@staticmethod
	def insertServiceName(account,service):
		print "heyayayayaa"

		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			insert_servicename_command = "INSERT INTO FireproofServices (masterid,ServiceName) VALUES (%s,%s)"
			#cur.execute(insert_servicename_command,(self.id_num,service.service_name))
			cur.execute(insert_servicename_command,(account.id_num,"Facebook"))

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
			cur.execute("CREATE TABLE FireproofServices (id INT(6) PRIMARY KEY AUTO_INCREMENT,masterid INT(6),ServiceName VARCHAR(30) NOT NULL)")


	@staticmethod
	def createServiceAccountsTable():
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			cur.execute("CREATE TABLE FireproofServicesAccounts (id INT(6) PRIMARY KEY AUTO_INCREMENT,serviceid INT(6),\
				masterid INT(6),ServiceUsername VARCHAR(30) NOT NULL,ServicePassword VARCHAR(30) NOT NULL)")		