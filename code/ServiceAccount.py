class ServiceAccount:

	def __init__(self,username,password):
		self.username = username
		self.password = password

		#self.username_enc
		#self.password_enc

	@staticmethod
	def insertServiceAccount(account,service):
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			insert_serviceaccount_command = "INSERT INTO FireproofServicesAccounts (serviceid,masterid,username,password) VALUES (%s,%s,%s,%s)"
			#cur.execute(insert_servicename_command,(self.id_num,service.service_name))
			cur.execute(insert_serviceaccount_command,(service.id_num,account.id_num,service.username,service.password))
