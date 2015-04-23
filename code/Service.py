import MySQLdb as mdb
from config import *
from AESCipher import *
from FireproofProgram import *
from ServiceAccount import *

TITLE_FONT = ("Helvetica", 18, "bold")
TEXT_FONT = ("Helvetica", 8, "bold")

class Service:
	
	ServiceCount = 1
	
	def __init__(self,service_name,account_owner,service_accounts=[]):
		"""Constructor that initializes a Service object

		:param service_name: name of the service
		:param account_owner: master account who owns this service
		:param service_accounts: all of the login accounts associated with this service

		:return: A Service object which store the name of the service, the owner, all of its accounts, and encrypted information
		"""
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
		"""Inserts the encrypted Service into the database by matching it with the master account's primary id

		:param account: The master account who owns this service
		"""

		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			insert_servicename_command = "INSERT INTO FireproofServices (id,masterid,ServiceName) VALUES (%s,%s,%s)"
			#cur.execute(insert_servicename_command,(self.id_num,service.service_name))
			cur.execute(insert_servicename_command,(service.id_num,account.id_num,service.service_name_enc))

	@staticmethod
	def retrieveServiceNameId(account,service):
		"""Retrieves the primary id of the service from the database

		:param account: The master account who owns this service
		:return: Primary id of the service
		:rtype: int
		"""

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
		"""Allows the user to update their existing services"""
		
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
		"""Initializes the FireproofServices table in our database"""
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			cur.execute("DROP TABLE IF EXISTS FireproofServices")
			cur.execute("CREATE TABLE FireproofServices (id INT(6) PRIMARY KEY,masterid INT(6),ServiceName VARCHAR(30) NOT NULL)")

	@staticmethod
	def confirmRemoveService(frame,controller):
		""" This function activates when the user clicks the delete button.
		It provides a popup window that confirms the user would like to
		delete the account. If the user clicks yes, then it deletes the
		account and returns to the main screen. If the user clicks no,
		the account is untouched and the user is returned to the Remove
		Service page frame.
		"""
		result = tkMessageBox.askquestion("Delete", "Are you sure?", icon='warning')
		if result == 'yes':
			print "Deleted!"
			index_to_delete = frame.CurrentServices.curselection()[0]

			service_page_frame = controller.getFrame(controller.ServicesPage)
			service_page_frame.removeFromCurrentServicesListBox(index_to_delete)

			service_page_frame = controller.getFrame(controller.AddNewServicePage)
			service_page_frame.removeFromExistingServicesListBox(index_to_delete)			


		else:
			print "Returning you to main screen"
		controller.show_frame(controller.ServicesPage)

	@staticmethod
	def addService(username,password,servicename,frame,controller):
		""" This function grabs the information from the provided fields
		and adds it to the database under the user's main account. It then
		clears the fields on this frame, and redirects the user to the 
		main page.			
		"""
		print "Service:", servicename
		print "Username:", username
		print "Password:", password
		
		# ***** WHY DOESN'T THIS WORK *****
		service_page_frame = controller.getFrame(controller.ServicesPage)
		service_page_frame.addToCurrentServicesListBox(servicename)

		service_page_frame = controller.getFrame(controller.AddNewServicePage)
		service_page_frame.addToExistingServicesListBox(servicename)		
		#add_to_existing.insert(END, servicename)
		
		service_account = ServiceAccount(username,password,controller.current_account)

		service = Service(servicename,controller.current_account,[service_account])

		controller.current_account.service_name_list += [service]

		service.insertServiceName(controller.current_account,service)
		ServiceAccount.insertServiceAccount(controller.current_account,service,service_account)
		#app.update()
		
		frame.username_input_form.delete(0, 'end')
		frame.password_input_form.delete(0, 'end')
		frame.service_input_form.delete(0, 'end')
		
		controller.show_frame(controller.ServicesPage)		

	@staticmethod
	def addServiceChecker(username,password,servicename,frame,controller):
		""" This function checks that all the fields on this frame
		have been filled out. If a field is blank, it creates a popup
		window alerting the user to the blank field. If all fields
		are filled out, it proceeds to call addService()
		"""
		if (servicename) == "":
			tkMessageBox.showinfo("Error","Please enter a service name.")
		elif (username) == "":
			tkMessageBox.showinfo("Error","Please enter a valid username.")
		elif (password) == "":
			tkMessageBox.showinfo("Error","Please enter a valid password.")
		else:
			Service.addService(username,password,servicename,frame,controller)

	@staticmethod
	def viewService(service_index,frame,controller):
		y_coordinate_u = 380
		y_coordinate_p = 380
		x_coordinate_u = 200
		x_coordinate_p = 300

		service_info_page_frame = controller.getFrame(controller.ServiceInfoPage)

		service = controller.current_account.service_name_list[service_index]
		label = tk.Label(service_info_page_frame, text=service.service_name, font=TITLE_FONT)
		label.place(bordermode=OUTSIDE,x=100,y=150)		
		for account in service.service_accounts:
			username_label = tk.Label(service_info_page_frame, text=account.username, font=TEXT_FONT)
			username_label.place(bordermode=OUTSIDE,x=x_coordinate_u,y=y_coordinate_u)
			y_coordinate_u += 20

			password_label = tk.Label(service_info_page_frame, text=account.password, font=TEXT_FONT)
			password_label.place(bordermode=OUTSIDE,x=x_coordinate_p,y=y_coordinate_p)
			y_coordinate_p += 20

		controller.show_frame(controller.ServiceInfoPage)
		
	@staticmethod
	def populateEditService(service_index, frame, controller):
		y_coordinate_u = 160
		x_coordinate_u = 210
		y_coordinate_p = 190
		x_coordinate_p = 210
		
		service_info_page_frame = controller.getFrame(controller.EditPage)
		
		service = controller.current_account.service_name_list[service_index]
		label = tk.Label(service_info_page_frame, text=service.service_name)
		label.place(bordermode=OUTSIDE, x=210, y=120)
		for account in service.service_accounts:
			username_label = tk.Label(service_info_page_frame, text=account.username)
			username_label.place(bordermode=OUTSIDE,x=x_coordinate_u, y=y_coordinate_u)
			y_coordinate_u += 20
			
			password_label = tk.Label(service_info_page_frame, text=account.password)
			password_label.place(bordermode=OUTSIDE,x=x_coordinate_p, y=y_coordinate_p)
			y_coordinate_p += 20
		controller.show_frame(controller.EditPage)

	#we need this, though it has to populate from the database for information, so most of this won't work
	@staticmethod
	def transitionFromInfoToEdit(service_index, frame, controller):
		service_info_page_frame = controller.getFrame(controller.EditPage)
		service = controller.current_account.service_name_list[service_index]
		
		label = tk.Label(service_info_page_frame, text=service.servicename)
		label.place(bordermode=OUTSIDE, x=210, y=120)
		for account in service.service_accounts:
			username_label = tk.Label(service_info_page_frame, text=account.username)
			username_label.place(bordermode=OUTSIDE,x=x_coordinate_u, y=y_coordinate_u)
			y_coordinate_u += 20
			
			password_label = tk.Label(service_info_page_frame, text=account.password)
			password_label.place(bordermode=OUTSIDE,x=x_coordinate_p, y=y_coordinate_p)
			y_coordinate_p += 20
		controller.show_frame(controller.EditPage)
