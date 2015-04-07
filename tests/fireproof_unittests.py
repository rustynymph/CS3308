import unittest
from FireproofProgram import *

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
    def test_accountCreation1(self):
        account = TestFireproofMethods.account1
        self.assertIsInstance(account,MasterAccount)  

    def test_accountCreation2(self):
        account = TestFireproofMethods.account2
        self.assertIsInstance(account,MasterAccount) 

    def test_accountCreation3(self):
        account = TestFireproofMethods.account3
        self.assertIsInstance(account,MasterAccount) 

    def test_accountCreation4(self):
        account = TestFireproofMethods.account4
        self.assertIsInstance(account,MasterAccount)  

    def test_accountCreation5(self):
        account = TestFireproofMethods.account5
        self.assertIsInstance(account,MasterAccount) 

    def test_accountCreation6(self):
        account = TestFireproofMethods.account6
        self.assertIsInstance(account,MasterAccount)                                         

    #test that the ".username" attribute for MasterAccount is set to the correct username
    def test_accountUsernameAttr1(self):
        givenName = TestFireproofMethods.accountUsernames[0]
        attrName = TestFireproofMethods.accountList[0].username
        self.assertEqual(givenName,attrName)

    def test_accountUsernameAttr2(self):
        givenName = TestFireproofMethods.accountUsernames[1]
        attrName = TestFireproofMethods.accountList[1].username
        self.assertEqual(givenName,attrName)

    def test_accountUsernameAttr3(self):
        givenName = TestFireproofMethods.accountUsernames[2]
        attrName = TestFireproofMethods.accountList[2].username
        self.assertEqual(givenName,attrName)

    def test_accountUsernameAttr4(self):
        givenName = TestFireproofMethods.accountUsernames[3]
        attrName = TestFireproofMethods.accountList[3].username
        self.assertEqual(givenName,attrName)

    def test_accountUsernameAttr5(self):
        givenName = TestFireproofMethods.accountUsernames[4]
        attrName = TestFireproofMethods.accountList[4].username
        self.assertEqual(givenName,attrName)

    def test_accountUsernameAttr6(self):
        givenName = TestFireproofMethods.accountUsernames[5]
        attrName = TestFireproofMethods.accountList[5].username
        self.assertEqual(givenName,attrName)

    #test that the ".password" attribute for MasterAccount is set to the correct password
    def test_accountPasswordAttr1(self):
        givenName = TestFireproofMethods.accountPasswords[0]
        attrName = TestFireproofMethods.accountList[0].password
        self.assertEqual(givenName,attrName)

    def test_accountPasswordAttr2(self):
        givenName = TestFireproofMethods.accountPasswords[1]
        attrName = TestFireproofMethods.accountList[1].password
        self.assertEqual(givenName,attrName)

    def test_accountPasswordAttr3(self):
        givenName = TestFireproofMethods.accountPasswords[2]
        attrName = TestFireproofMethods.accountList[2].password
        self.assertEqual(givenName,attrName)

    def test_accountPasswordAttr4(self):
        givenName = TestFireproofMethods.accountPasswords[3]
        attrName = TestFireproofMethods.accountList[3].password
        self.assertEqual(givenName,attrName)

    def test_accountPasswordAttr5(self):
        givenName = TestFireproofMethods.accountPasswords[4]
        attrName = TestFireproofMethods.accountList[4].password
        self.assertEqual(givenName,attrName)

    def test_accountPasswordAttr6(self):
        givenName = TestFireproofMethods.accountPasswords[5]
        attrName = TestFireproofMethods.accountList[5].password
        self.assertEqual(givenName,attrName)  

  #TESTING OUR ENCRYPTION SUITE

    #test that the ".username_enc" attribute for MasterAccount does not equal the given username
    def test_encryptedUsernameAttr1(self):
        givenUsername = TestFireproofMethods.accountUsernames[0]
        encryptedUsername = TestFireproofMethods.accountEncryptedUsernames[0]
        self.assertNotEqual(givenUsername,encryptedUsername)

    def test_encryptedUsernameAttr2(self):
        givenUsername = TestFireproofMethods.accountUsernames[1]
        encryptedUsername = TestFireproofMethods.accountEncryptedUsernames[1]
        self.assertNotEqual(givenUsername,encryptedUsername)

    def test_encryptedUsernameAttr3(self):
        givenUsername = TestFireproofMethods.accountUsernames[2]
        encryptedUsername = TestFireproofMethods.accountEncryptedUsernames[2]
        self.assertNotEqual(givenUsername,encryptedUsername)                

    def test_encryptedUsernameAttr4(self):
        givenUsername = TestFireproofMethods.accountUsernames[3]
        encryptedUsername = TestFireproofMethods.accountEncryptedUsernames[3]
        self.assertNotEqual(givenUsername,encryptedUsername)

    def test_encryptedUsernameAttr5(self):
        givenUsername = TestFireproofMethods.accountUsernames[4]
        encryptedUsername = TestFireproofMethods.accountEncryptedUsernames[4]
        self.assertNotEqual(givenUsername,encryptedUsername)

    def test_encryptedUsernameAttr6(self):
        givenUsername = TestFireproofMethods.accountUsernames[5]
        encryptedUsername = TestFireproofMethods.accountEncryptedUsernames[5]
        self.assertNotEqual(givenUsername,encryptedUsername)                

    #test that the ".password_enc" attribute for MasterAccount does not equal the given password
    def test_encryptedPasswordAttr1(self):
        givenPassword = TestFireproofMethods.accountPasswords[0]
        encryptedPassword = TestFireproofMethods.accountEncryptedPasswords[0]
        self.assertNotEqual(givenPassword,encryptedPassword)

    def test_encryptedPasswordAttr2(self):
        givenPassword = TestFireproofMethods.accountPasswords[1]
        encryptedPassword = TestFireproofMethods.accountEncryptedPasswords[1]
        self.assertNotEqual(givenPassword,encryptedPassword)

    def test_encryptedPasswordAttr3(self):
        givenPassword = TestFireproofMethods.accountPasswords[2]
        encryptedPassword = TestFireproofMethods.accountEncryptedPasswords[2]
        self.assertNotEqual(givenPassword,encryptedPassword)                

    def test_encryptedPasswordAttr4(self):
        givenPassword = TestFireproofMethods.accountPasswords[3]
        encryptedPassword = TestFireproofMethods.accountEncryptedPasswords[3]
        self.assertNotEqual(givenPassword,encryptedPassword)

    def test_encryptedPasswordAttr5(self):
        givenPassword = TestFireproofMethods.accountPasswords[4]
        encryptedPassword = TestFireproofMethods.accountEncryptedPasswords[4]
        self.assertNotEqual(givenPassword,encryptedPassword)

    def test_encryptedPasswordAttr6(self):
        givenPassword = TestFireproofMethods.accountPasswords[5]
        encryptedPassword = TestFireproofMethods.accountEncryptedPasswords[5]
        self.assertNotEqual(givenPassword,encryptedPassword)                


    #test that when we encrypt and then decrypt our username, we get the original username back
    def test_encryptionDecryptionUsername1(self):
        account = TestFireproofMethods.accountList[0]
        givenUsername = account.username
        encryptedUsername = account.username_enc
        key = account.key
        iv = account.iv
        decryptedUsername = MasterAccount.decryptCredentials(key,iv,encryptedUsername)
        self.assertEqual(givenUsername,decryptedUsername)

    def test_encryptionDecryptionUsername2(self):
        account = TestFireproofMethods.accountList[1]
        givenUsername = account.username
        encryptedUsername = account.username_enc
        key = account.key
        iv = account.iv
        decryptedUsername = MasterAccount.decryptCredentials(key,iv,encryptedUsername)
        self.assertEqual(givenUsername,decryptedUsername)

    def test_encryptionDecryptionUsername3(self):
        account = TestFireproofMethods.accountList[2]
        givenUsername = account.username
        encryptedUsername = account.username_enc
        key = account.key
        iv = account.iv
        decryptedUsername = MasterAccount.decryptCredentials(key,iv,encryptedUsername)
        self.assertEqual(givenUsername,decryptedUsername)

    def test_encryptionDecryptionUsername4(self):
        account = TestFireproofMethods.accountList[3]
        givenUsername = account.username
        encryptedUsername = account.username_enc
        key = account.key
        iv = account.iv
        decryptedUsername = MasterAccount.decryptCredentials(key,iv,encryptedUsername)
        self.assertEqual(givenUsername,decryptedUsername)

    def test_encryptionDecryptionUsername5(self):
        account = TestFireproofMethods.accountList[4]
        givenUsername = account.username
        encryptedUsername = account.username_enc
        key = account.key
        iv = account.iv
        decryptedUsername = MasterAccount.decryptCredentials(key,iv,encryptedUsername)
        self.assertEqual(givenUsername,decryptedUsername)                                

    def test_encryptionDecryptionUsername6(self):
        account = TestFireproofMethods.accountList[5]
        givenUsername = account.username
        encryptedUsername = account.username_enc
        key = account.key
        iv = account.iv
        decryptedUsername = MasterAccount.decryptCredentials(key,iv,encryptedUsername)
        self.assertEqual(givenUsername,decryptedUsername)

    #test that when we encrypt and then decrypt our password, we get the original password back
    def test_encryptionDecryptionPassword1(self):
        account = TestFireproofMethods.accountList[0]
        givenPassword = account.password
        encryptedPassword = account.password_enc
        key = account.key
        iv = account.iv
        decryptedPassword = MasterAccount.decryptCredentials(key,iv,encryptedPassword)
        self.assertEqual(givenPassword,decryptedPassword)

    def test_encryptionDecryptionPassword2(self):
        account = TestFireproofMethods.accountList[1]
        givenPassword = account.password
        encryptedPassword = account.password_enc
        key = account.key
        iv = account.iv
        decryptedPassword = MasterAccount.decryptCredentials(key,iv,encryptedPassword)
        self.assertEqual(givenPassword,decryptedPassword)

    def test_encryptionDecryptionPassword3(self):
        account = TestFireproofMethods.accountList[2]
        givenPassword = account.password
        encryptedPassword = account.password_enc
        key = account.key
        iv = account.iv
        decryptedPassword = MasterAccount.decryptCredentials(key,iv,encryptedPassword)
        self.assertEqual(givenPassword,decryptedPassword)

    def test_encryptionDecryptionPassword4(self):
        account = TestFireproofMethods.accountList[3]
        givenPassword = account.password
        encryptedPassword = account.password_enc
        key = account.key
        iv = account.iv
        decryptedPassword = MasterAccount.decryptCredentials(key,iv,encryptedPassword)
        self.assertEqual(givenPassword,decryptedPassword)

    def test_encryptionDecryptionPassword5(self):
        account = TestFireproofMethods.accountList[4]
        givenPassword = account.password
        encryptedPassword = account.password_enc
        key = account.key
        iv = account.iv
        decryptedPassword = MasterAccount.decryptCredentials(key,iv,encryptedPassword)
        self.assertEqual(givenPassword,decryptedPassword)                                

    def test_encryptionDecryptionPassword6(self):
        account = TestFireproofMethods.accountList[5]
        givenPassword = account.password
        encryptedPassword = account.password_enc
        key = account.key
        iv = account.iv
        decryptedPassword = MasterAccount.decryptCredentials(key,iv,encryptedPassword)
        self.assertEqual(givenPassword,decryptedPassword)

if __name__ == '__main__':
  unittest.main()
