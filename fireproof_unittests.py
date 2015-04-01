import unittest
from FireproofFunctions import *
from FireproofProgram import *
from MasterAccount import *

class TestFireproofMethods(unittest.TestCase):

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

#TESTING OUT MASTERACCOUNT CONSTRUCTOR

  #test that all the accounts are probably instantiated as MasterAccount
    def test_accountCreation(self):
      for account in TestFireproofMethods.accountList:
        self.assertIsInstance(account,MasterAccount)  

    #test that the ".username" attribute for MasterAccount is set to the correct username
    def test_accountUsernameAttr(self):
      for i in range (0,6):
        givenName = TestFireproofMethods.accountUsernames[i]
        attrName = TestFireproofMethods.accountList[i].username
        self.assertEqual(givenName,attrName)

    #test that the ".password" attribute for MasterAccount is set to the correct password
    def test_accountPasswordAttr(self):
      for i in range (0,6):
        givenPassword = TestFireproofMethods.accountPasswords[i]
        attrPassword = TestFireproofMethods.accountList[i].password
        self.assertEqual(givenPassword,attrPassword)    

  #TESTING OUR ENCRYPTION SUITE

    #test that the ".username_enc" attribute for MasterAccount does not equal the given username
    def test_encryptedUsernameAttr(self):
      for i in range(0,6):
        givenUsername = TestFireproofMethods.accountUsernames[i]
        encryptedUsername = TestFireproofMethods.accountEncryptedUsernames[i]
        self.assertNotEqual(givenUsername,encryptedUsername)

    #test that the ".password_enc" attribute for MasterAccount does not equal the given password
    def test_encryptedPasswordAttr(self):
      for i in range(0,6):
        givenPassword = TestFireproofMethods.accountPasswords[i]
        encryptedPassword = TestFireproofMethods.accountEncryptedPasswords[i]
        self.assertNotEqual(givenPassword,encryptedPassword)

    #test that when we encrypt and then decrypt our username, we get the original username back
    def test_encryptionDecryptionUsername(self):
      for i in range(0,6):
        account = TestFireproofMethods.accountList[i]
        givenUsername = account.username
        encryptedUsername = account.username_enc
        key = account.key
        iv = account.iv
        decryptedUsername = MasterAccount.decryptCredentials(key,iv,encryptedUsername)
        self.assertEqual(givenUsername,decryptedUsername)

    #test that when we encrypt and then decrypt our password, we get the original password back
    def test_encryptionDecryptionPassword(self):
      for i in range(0,6):
        account = TestFireproofMethods.accountList[i]
        givenPassword = account.password
        encryptedPassword = account.password_enc
        key = account.key
        iv = account.iv
        decryptedPassword = MasterAccount.decryptCredentials(key,iv,encryptedPassword)
        self.assertEqual(givenPassword,decryptedPassword)

    def test_encryptionLength(self):

if __name__ == '__main__':
  unittest.main()
