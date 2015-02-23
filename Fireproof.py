#!/usr/bin/python

import MySQLdb as mdb
import sys
from MasterAccount import *


def main():

	masterusername = sys.argv[1]
	masterpassword = sys.argv[2]
	
	account = MasterAccount(masterusername,masterpassword,0)
	MasterAccount.insertMasterAccount(account)
	MasterAccount.retrieveMasterAccount(account)

main()
