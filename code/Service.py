import MySQLdb as mdb
from config import *
from AESCipher import *
from FireproofProgram import *
from ServiceAccount import *

TITLE_FONT = ("Helvetica", 18, "bold")
TEXT_FONT = ("Helvetica", 8, "bold")

class Service:
	
	ServiceCount = 1
	stored_index = None
	
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
	def insertServiceName(account,service): #insertServiceIntoDatabase
		"""Inserts the encrypted Service into the database by matching it with the master account's primary id

		:param account: The master account who owns this service
		"""

		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

		with con:
			cur = con.cursor()
			insert_servicename_command = "INSERT INTO FireproofServices (id,masterid,ServiceName) VALUES (%s,%s,%s)"
			#cur.execute(insert_servicename_command,(self.id_num,service.service_name))
			cur.execute(insert_servicename_command,(service.id_num,account.id_num,service.service_name_enc))
	
	#WORK IN PROGRESS; also needs to delete from other table(fireproofserviceaccounts?) as well
	@staticmethod
	def removeServiceFromDatabase(account,service):
		"""Deletes the specified Service from the database by matching its
		service id and master account's primary id
		
		:param account: The master account who owns this service
		"""
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);
		with con:
			cur = con.cursor()
			delete_service_command = "DELETE FROM FireproofServices WHERE id=%s AND masterid=%s"
			cur.execute(delete_service_command, (service.id_num, account.id_num))
	
	@staticmethod
	def changeServiceUsername(account, service, new_username):
		"""Updates the specified service's stored username to be the newly provided username.
		
		:param account: The master account that owns this service
		"""
		con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);
		with con:
			cur = con.cursor()
			change_username_command= "UPDATE FireproofServices SET ServiceName=%s WHERE id=%s AND masterid=%s"
			cur.execute(change_username_command, (new_username, service.id_num, account.id_num))
	
	@staticmethod
	def retrieveServiceNameId(account,service): #retrieveServiceId
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
	def changeService(account,service): #updateService
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
	def createServiceTable(): #createFireproofServicesTable
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
		print "SELECTION #:", frame.CurrentServices.curselection()[0]
		result = tkMessageBox.askquestion("Delete", "Are you sure?", icon='warning')
		if result == 'yes':
			index_to_delete = frame.CurrentServices.curselection()[0]
			service = controller.current_account.service_name_list[index_to_delete]
			controller.current_account.service_name_list.remove(service)

			Service.removeServiceFromDatabase(controller.current_account,service)
			ServiceAccount.removeServiceAccountFromDatabase(controller.current_account,service)

			service_page_frame = controller.getFrame(controller.ServicesPage)
			service_page_frame.removeFromCurrentServicesListBox(index_to_delete)

			service_page_frame = controller.getFrame(controller.AddNewServicePage)
			service_page_frame.removeFromExistingServicesListBox(index_to_delete)			
			print "Deleted!"
		else:
			print "Returning you to main screen"
		controller.show_frame(controller.ServicesPage)

	@staticmethod
	def addService(username,password,servicename,frame,controller): #gatherServiceInformation
		""" This function grabs the information from the provided fields
		and adds it to the database under the user's main account. It then
		clears the fields on this frame, and redirects the user to the 
		main page.			
		"""
		print "Service:", servicename
		print "Username:", username
		print "Password:", password
		
		service_page_frame = controller.getFrame(controller.ServicesPage)
		service_page_frame.addToCurrentServicesListBox(servicename)

		service_page_frame = controller.getFrame(controller.AddNewServicePage)
		service_page_frame.addToExistingServicesListBox(servicename)		
		
		service_account = ServiceAccount(username,password,controller.current_account)

		service = Service(servicename,controller.current_account,[service_account])

		controller.current_account.service_name_list += [service]

		service.insertServiceName(controller.current_account,service)
		ServiceAccount.insertServiceAccount(controller.current_account,service,service_account)
		
		frame.username_input_form.delete(0, 'end')
		frame.password_input_form.delete(0, 'end')
		frame.service_input_form.delete(0, 'end')
		
		controller.show_frame(controller.ServicesPage)		

	@staticmethod
	def editServiceChecker(username,password,confirmpassword,servicename,frame,controller): #checkerForGatherServiceInformation
		""" This function checks that all the fields on this frame
		have been filled out. If a field is blank, it creates a popup
		window alerting the user to the blank field. If all fields
		are filled out, it proceeds to call addService()
		"""
		if (username) == "" and (password) == "" and (confirmpassword) == "":
			tkMessageBox.showinfo("Error","Please enter a valid username or password.")
		elif (password) != "" and (confirmpassword) == "":
			tkMessageBox.showinfo("Error","Please enter a valid confirmed password.")
		elif (password) == "" and (confirmpassword) != "":
			tkMessageBox.showinfo("Error","Please enter a valid password.")
		else:
			Service.addService(username,password,servicename,frame,controller)

	@staticmethod
	def addServiceChecker(username,password,servicename,frame,controller): #checkerForGatherServiceInformation
		""" This function checks that the fields on this frame
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
	def viewService(service_index,frame,controller): #populateViewService #populateServiceInfoPage
		"""
		This function takes the Listbox index from the ServicesPage and
		uses it to display the service's name, username and password for
		the user. The username and password are unencrypted before being
		displayed.
		
		:param controller: Tkinter GUI manager
		:param frame: Tkinter frame widget
		:param service_index: Listbox index for the service
		"""
		frame.CurrentServices.update()
		service_info_page_frame = controller.getFrame(controller.ServiceInfoPage)
		print "SELECTION #:", frame.CurrentServices.curselection()[0]
		#for populateEditServiceFromServiceInfo
		Service.stored_index = service_index
		service = controller.current_account.service_name_list[service_index]
		label = tk.Label(service_info_page_frame, text=service.service_name)
		label.place(bordermode=OUTSIDE,x=190,y=140)		
		for account in service.service_accounts:
			username_label = tk.Label(service_info_page_frame, text=account.username)
			username_label.place(bordermode=OUTSIDE,x=190,y=165)

			password_label = tk.Label(service_info_page_frame, text=account.password)
			password_label.place(bordermode=OUTSIDE,x=190,y=190)
		frame.CurrentServices.update()
		controller.show_frame(controller.ServiceInfoPage)
		
	@staticmethod
	def populateEditServiceFromServiceInfo(frame, controller):
		"""
		This function takes the stored Listbox index from the viewService
		function call and uses it to display the service's name, username 
		and password for the user so the user can decide which field(s), 
		if any, they would like to change. The username and password are 
		unencrypted before being displayed.
		
		:param controller: Tkinter GUI manager
		:param frame: Tkinter frame widget
		"""
		service = controller.current_account.service_name_list[Service.stored_index]
		Service.current_service = service

		edit_page_frame = controller.getFrame(controller.EditPage)

		label = tk.Label(edit_page_frame, text=service.service_name)
		label.place(bordermode=OUTSIDE, x=210, y=140)

		for account in service.service_accounts:
			username_label = tk.Label(edit_page_frame, text=account.username)
			username_label.place(bordermode=OUTSIDE,x=210, y=165)

			password_label = tk.Label(edit_page_frame, text=account.password)
			password_label.place(bordermode=OUTSIDE,x=210, y=190)
		controller.show_frame(controller.EditPage)
		
	@staticmethod
	def populateEditService(service_index, frame, controller):
		"""
		This function takes the Listbox index from the ServicesPage and
		uses it to display the service's name, username and password for
		the user so the user can decide which field(s), if any, they would
		like to change. The username and password are unencrypted before 
		being displayed.
		
		:param controller: Tkinter GUI manager
		:param frame: Tkinter frame widget
		:param service_index: Listbox index for the service
		"""
		edit_page_frame = controller.getFrame(controller.EditPage)
		
		service = controller.current_account.service_name_list[service_index]
		Service.current_service = service
		label = tk.Label(edit_page_frame, text=service.service_name)
		label.place(bordermode=OUTSIDE, x=210, y=140)
		for account in service.service_accounts:
			username_label = tk.Label(edit_page_frame, text=account.username)
			username_label.place(bordermode=OUTSIDE,x=210, y=165)
			
			password_label = tk.Label(edit_page_frame, text=account.password)
			password_label.place(bordermode=OUTSIDE,x=210, y=190)
		controller.show_frame(controller.EditPage)
		
	@staticmethod
	def hideFields(self, controller): #clearFieldsInServicesPage
		"""
		This function clears the fields in the ViewService page.
		
		:param self: the frame calling hideFields
		:param controller: Tkinter GUI manager
		"""
		hide_service_label = Label(self,text="                           ",)
		hide_service_label.place(bordermode=OUTSIDE,x=190,y=140)	
	
		hide_username_label = Label(self, text="                         ")
		hide_username_label.place(bordermode=OUTSIDE,x=190,y=165)
	
		hide_password_label = Label(self, text="                         ")
		hide_password_label.place(bordermode=OUTSIDE,x=190,y=190)
	
		controller.show_frame(controller.ServicesPage)	

	@staticmethod
	def hideFieldsFromEdit(self, controller): #clearFieldsInEditPage
		"""
		This function clears the fields in the EditService page.
		
		:param self: the frame calling hideFields
		:param controller: Tkinter GUI manager
		"""
		hide_service_label = Label(self,text="                           ")
		hide_service_label.place(bordermode=OUTSIDE,x=190,y=140)	
	
		hide_username_label = Label(self, text="                         ")
		hide_username_label.place(bordermode=OUTSIDE,x=190,y=165)
	
		hide_password_label = Label(self, text="                         ")
		hide_password_label.place(bordermode=OUTSIDE,x=190,y=190)
	
		controller.show_frame(controller.EditPage)	

	@staticmethod
	def saveNewServiceInfo(frame,controller,new_username,new_password,confirm_password):
		ServiceAccount.changeServiceAccountUsername(controller.current_account,Service.current_service,new_username)
		ServiceAccount.changeServicePassword(controller.current_account,Service.current_service,new_password)
		controller.show_frame(controller.ServicesPage)
