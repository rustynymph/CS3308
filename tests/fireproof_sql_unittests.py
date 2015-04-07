import unittest
from FireproofProgram import *


class TestFireproofSQL(unittest.TestCase):

	account1 = MasterAccount('MyUsername','MyPassword')
	account2 = MasterAccount('MyUsername','MyPassword')
	account3 = MasterAccount('Shmoopi','smileyface')
	account4 = MasterAccount('hi','12345678')
	account5 = MasterAccount('random','________')
	account6 = MasterAccount('samename','samename')
	accountUsernames = ['MyUsername','MyUsername','Shmoopi','hi','random','samename']
	accountPasswords = ['MyPassword','MyPassword','smileyface','12345678','________','samename']
	accountList = [account1,account2,account3,account4,account5,account6]
	accountEncryptedUsernames = [account.username_enc for account in accountList]
	accountEncryptedPasswords = [account.password_enc for account in accountList]    
	#con = mdb.connect('localhost','unittestUser','unittestPassword','TestDB');
	con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);
	
	with con:
		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS FireproofAccountLogin")
		cur.execute("CREATE TABLE FireproofAccountLogin (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,UserName VARCHAR(30) NOT NULL,\
			PasswordName VARCHAR(30) NOT NULL)")

		for i in range(0,6):
			account = accountList[i]
			cur.execute("INSERT INTO FireproofAccountLogin (UserName,PasswordName) VALUES (%s,%s)",(account.username_enc,account.password_enc))

	def test_accountRetrieval(self):
		con = TestFireproofSQL.con
		with con:
			cur = con.cursor()	
			for i in range(0,6):
				account = TestFireproofSQL.accountList[i]
				cur.execute("SELECT Id FROM FireproofAccountLogin WHERE (UserName,PasswordName) = (%s,%s)", (account.username_enc,account.password_enc))
				id_number = cur.fetchone()
				self.assertIsNotNone(id_number)
			

if __name__ == '__main__':
  unittest.main()
