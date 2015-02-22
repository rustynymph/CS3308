#!/usr/bin/python

import MySQLdb as mdb
import sys
from User import *
#from Crypto.Cipher import AES


def main():

	masterusername = sys.argv[1]
	masterpassword = sys.argv[2]
		
	return masterAccount(masterusername,masterpassword,0)

main()
