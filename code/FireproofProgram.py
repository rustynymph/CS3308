import Tkinter as tk
import tkMessageBox
from Tkinter import *
from LoginFunctions import *
import MySQLdb as mdb
from config import *
from Service import *
from ServiceAccount import *


TITLE_FONT = ("Helvetica", 18, "bold")
TEXT_FONT = ("Helvetica", 8, "bold")
class Fireproof(tk.Tk):
	
	#current_account = None
	
	def __init__(self, *args, **kwargs):
		""" Initializes the main Tkinter frame container.
		Also places the Fireproof graphic onto every frame.

        :param tk.TK: Toplevel widget of Tkinter which represents the main window of the Fireproof appliation
		"""
		tk.Tk.__init__(self, *args, **kwargs)

		# the container is where we'll stack a bunch of frames
		# on top of each other, then the one we want visible
		# will be raised above the others
		self.current_account = None

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		
		fireproof_image = PhotoImage(file="../images/fireproof.png")
		fireproof_banner = Label(image=fireproof_image)
		fireproof_banner.image = fireproof_image
		fireproof_banner.place(bordermode=OUTSIDE,x=150,y=15)		

		self.frames = {}
		for F in (LoginPage, CreateAccountPage, ServicesPage, SettingsPage, ServiceInfoPage, AddNewServicePage, EditPage, RemoveServicePage):
			frame = F(container, self)
			self.frames[F] = frame
			# put all of the pages in the same location; 
			# the one on the top of the stacking order
			# will be the one that is visible.
			frame.grid(row=0, column=0, sticky="nsew")

		self.LoginPage = LoginPage
		self.CreateAccountPage = CreateAccountPage
		self.ServicesPage = ServicesPage
		self.SettingsPage = SettingsPage
		self.ServiceInfoPage = ServiceInfoPage
		self.AddNewServicePage = AddNewServicePage
		self.EditPage = EditPage
		self.RemoveServicePage = RemoveServicePage


		self.show_frame(LoginPage)

	def show_frame(self, c):
		""" This function changes frame (c) so it is visible to the user.

        :param c: Name of frame
		"""
		frame = self.frames[c]
		frame.tkraise()

	def getFrame(self, c):
		return self.frames[c]


class LoginPage(tk.Frame):
	def __init__(self, parent, controller):
		""" This initializes the login frame for the app. The login frame
		allows the user to sign in to an existing account, or create a new
		account.

        :param tk.Frame: Tkinter frame widget
		"""
		tk.Frame.__init__(self, parent) 

		username_form_label = Label(self,text="Username")
		username_form_label.place(bordermode=OUTSIDE,x=60,y=140)

		password_form_label = Label(self,text="Password")
		password_form_label.place(bordermode=OUTSIDE,x=60,y=190)
		
		self.username_input_form = Entry(self,bd=5)
		self.username_input_form.place(bordermode=OUTSIDE,x=180,y=140)

		self.password_input_form = Entry(self,bd=5,show="*")
		self.password_input_form.place(bordermode=OUTSIDE,x=180,y=190)
		
		
		login_button = Button(self, text ="Login", command= lambda: LoginFunctions.checkIfUser(self.username_input_form.get(),self.password_input_form.get(),self,controller))
		login_button.place(bordermode=OUTSIDE,x=292,y=240)		
		
		new_user_label = tk.Label(self, text="New User?", font=TEXT_FONT)
		new_user_label.place(bordermode=OUTSIDE,x=235,y=300)
		
		create_account_label = tk.Label(self, text="Click here to create an account", font=TEXT_FONT)
		create_account_label.place(bordermode=OUTSIDE,x=190,y=320)
		
		sign_up_button = Button(self, text ="Sign Up", command=lambda: controller.show_frame(CreateAccountPage))
		sign_up_button.place(bordermode=OUTSIDE,x=225,y=340)
				

class CreateAccountPage(tk.Frame):
	def __init__(self, parent, controller):
		""" This initializes the create account frame for the app. The create
		account frame allows the person to enter information that will be used
		to create a new account in the database.

        :param tk.Frame: Tkinter frame widget
		"""
		tk.Frame.__init__(self, parent)
		
		username_form_label = Label(self,text="Username")
		username_form_label.place(bordermode=OUTSIDE,x=60,y=140)

		password_form_label = Label(self,text="Password")
		password_form_label.place(bordermode=OUTSIDE,x=60,y=190)
		
		confirm_password_form_label = Label(self,text="Confirm Password")
		confirm_password_form_label.place(bordermode=OUTSIDE,x=60,y=240)

		username_input_form = Entry(self,bd=5)
		username_input_form.place(bordermode=OUTSIDE,x=180,y=140)

		password_input_form = Entry(self,bd=5,show="*")
		password_input_form.place(bordermode=OUTSIDE,x=180,y=190)
		
		confirm_password_input_form = Entry(self,bd=5,show="*")
		confirm_password_input_form.place(bordermode=OUTSIDE,x=180,y=240)
		
		def createAccount():
			""" This creates the user account when the create account 
			button is selected. It also clears the information from the 
			fields, and then displays the login page for the user.
			"""
			LoginFunctions.createLoginInfo(username_input_form.get(),password_input_form.get(),confirm_password_input_form.get())
			username_input_form.delete(0, 'end')
			password_input_form.delete(0, 'end')
			confirm_password_input_form.delete(0, 'end')
			controller.show_frame(LoginPage)
		
		create_account_button = Button(self, text ="Create Account", command=createAccount)
		create_account_button.place(bordermode=OUTSIDE,x=235,y=290)
		
		go_back_button = Button(self, text ="Back", command=lambda: controller.show_frame(LoginPage))
		go_back_button.place(bordermode=OUTSIDE,x=125,y=350)
		
		#tips = Label(self,text="Passwords should be at least 8 characters")
		#tips.place(bordermode=OUTSIDE,x=60,y=140)								
		
class ServicesPage(tk.Frame):


	def __init__(self, parent, controller):
		""" This initializes the services page frame for the app. This frame
		displays a list of the user's stored services, and provides buttons
		that allow the user to transition to other frames.

        :param tk.Frame: Tkinter frame widget
		"""
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)
		logout_button = Button(self, text="Logout", command=lambda: controller.show_frame(LoginPage))
		logout_button.place(bordermode=OUTSIDE,x=5,y=5)
		
		text_label = "Welcome! Here are your stored services:"
		ListboxLabel = Label(self, text = text_label)
		ListboxLabel.place(x=20, y=120)
		
		scrollbar = Scrollbar(self, orient=VERTICAL)
		scrollbar.pack(side=RIGHT, fill=Y)
		
		self.CurrentServices = Listbox(self)
		self.CurrentServices.pack()
		
		self.CurrentServices.config(borderwidth=4, height=14, width=38)
		scrollbar.config(command=self.CurrentServices.yview)
		
		self.CurrentServices.place(bordermode=OUTSIDE,x=20,y=145)
		scrollbar.place(x=335,y=145, height=230)
		
		change_password_button = Button(self, text="Settings", command=lambda: controller.show_frame(SettingsPage))
		change_password_button.place(bordermode=OUTSIDE,x=417,y=5)
		
		add_new_service_button = Button(self, text="Add a new service", command=lambda: controller.show_frame(AddNewServicePage))
		add_new_service_button.place(bordermode=OUTSIDE,x=355,y=365)
        
		edit_service_button = Button(self, text="     Edit service     ", command=lambda: controller.show_frame(EditPage))
		edit_service_button.place(bordermode=OUTSIDE,x=355,y=335)

		delete_service_button = Button(self, text="    Delete service   ", command=lambda: controller.show_frame(RemoveServicePage))
		delete_service_button.place(bordermode=OUTSIDE, x=355,y=305)
	
	def update_CurrentServices(self,string):
		self.CurrentServices.insert(END, string)

class SettingsPage(tk.Frame):
	def __init__(self, parent, controller):
		""" This initializes the settings page frame for the app. This frame
		provides the user with some buttons for adjusting the settings of
		the app.

        :param tk.Frame: Tkinter frame widget
		"""
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)
		
		#changepassword
		change_password_button = Button(self, text="Change Password", command=lambda: controller.show_frame(AddNewServicePage))
		change_password_button.place(bordermode=OUTSIDE,x=200,y=220)
		#changeusername
		change_password_button = Button(self, text="Change Username", command=lambda: controller.show_frame(AddNewServicePage))
		change_password_button.place(bordermode=OUTSIDE,x=200,y=250)
		
		back_button = Button(self, text="Back", command=lambda: controller.show_frame(ServicesPage))
		back_button.place(bordermode=OUTSIDE,x=200,y=280)
		
class ServiceInfoPage(tk.Frame):
	def __init__(self, parent, controller):
		""" This initializes the individual service page frames for the services
		that are stored on this account. This frame displays the stored username,
		password and name of the service. It also displays a button that allows
		the user to edit the information associated with this service.

        :param tk.Frame: Tkinter frame widget
		"""
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Service Information Page", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)
        
		edit_service_button = Button(self, text="    Edit this service    ", command=lambda: controller.show_frame(EditPage))

		edit_service_button.place(bordermode=OUTSIDE,x=355,y=365)
		
		back_button = Button(self, text="Back", command=lambda: controller.show_frame(ServicesPage))
		back_button.place(bordermode=OUTSIDE,x=200,y=280)

class EditPage(tk.Frame):
	def __init__(self, parent, controller):
		""" This initializes the edit page frame for the app. This frame
		displays the service name along with the current stored username
		and password, and allows the user to save a new username and 
		password for this service.

        :param tk.Frame: Tkinter frame widget
		"""
		tk.Frame.__init__(self, parent)
		# display service name
		service_form_label = Label(self,text="ServiceNameGoesHere")
		service_form_label.place(bordermode=OUTSIDE,x=60,y =120)
		
		curr_username_form_label = Label(self,text="Current Username:")
		curr_username_form_label.place(bordermode=OUTSIDE,x=60,y=160)
		
		curruser_label = Label(self,text="FOOBAR")
		curruser_label.place(bordermode=OUTSIDE,x=210,y=160)
		
		currpass_label = Label(self,text="BestPasswordEver1234")
		currpass_label.place(bordermode=OUTSIDE,x=210,y=190)
		
		curr_password_form_label = Label(self,text="Current Password:")
		curr_password_form_label.place(bordermode=OUTSIDE,x=60,y=190)
		
		# display current password; pull from DB
		
		username_form_label = Label(self,text="New Username")
		username_form_label.place(bordermode=OUTSIDE,x=60,y=235)
		username_input_form = Entry(self,bd=5)
		username_input_form.place(bordermode=OUTSIDE,x=210,y=230)
		
		password_form_label = Label(self,text="New Password")
		password_form_label.place(bordermode=OUTSIDE,x=60,y=270)
		password_input_form = Entry(self,bd=5,show="*")
		password_input_form.place(bordermode=OUTSIDE,x=210,y=265)
		
		confirm_password_label = Label(self,text="Confirm New Password")
		confirm_password_label.place(bordermode=OUTSIDE,x=60,y=305)
		confirm_password_input_form = Entry(self,bd=5,show="*")
		confirm_password_input_form.place(bordermode=OUTSIDE,x=210,y=300)
		
		back_button = Button(self, text="Cancel", command=lambda: controller.show_frame(ServicesPage))
		back_button.place(bordermode=OUTSIDE,x=150,y=350)
		
		save_button = Button(self, text="Save", command=lambda: controller.show_frame(ServicesPage))
		save_button.place(bordermode=OUTSIDE,x=250,y=350)

class RemoveServicePage(tk.Frame):
	def __init__(self, parent, controller):
		""" This initializes the remove services page frame for the app. 
		This frame provides a list of the current services saved to the
		user's account, and allows the user to select one for removal.

        :param tk.Frame: Tkinter frame widget
		"""
		tk.Frame.__init__(self, parent)
		
		existingForm = Label(self, text = "Choose a service to remove:")
		existingForm.place(bordermode=OUTSIDE, x=50, y=100)
		
		def ConfirmRemove():
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
			else:
				print "Returning you to main screen"
			controller.show_frame(ServicesPage)
		
		more_options_button = Button(self, text ="Remove Service", command=ConfirmRemove)
		more_options_button.place(bordermode=OUTSIDE,x=200,y=350)
		
		back_button = Button(self, text ="Back", command=lambda: controller.show_frame(ServicesPage))
		back_button.place(bordermode=OUTSIDE,x=125,y=350)

class AddNewServicePage(tk.Frame):
	def __init__(self, parent, controller):
		""" This initializes the add new service page frame for the app.
		This page allows the user to enter in the service name, along with
		the username and password for that service, to be stored in a 
		database.

        :param tk.Frame: Tkinter frame widget
		"""
		tk.Frame.__init__(self, parent)
		
		existingForm = Label(self, text = "Add new service:")
		existingForm.place(bordermode=OUTSIDE, x=50, y=100)
		
		service_form_label = Label(self, text = "Service Name")
		service_form_label.place(bordermode=OUTSIDE, x=50, y=140)
		
		service_input_form = Entry(self, bd=5)
		service_input_form.place(bordermode=OUTSIDE, x=200, y=140)
		
		username_form_label = Label(self, text = "Username")
		username_form_label.place(bordermode=OUTSIDE, x=50, y=180)
		
		password_form_label = Label(self, text = "Password")
		password_form_label.place(bordermode=OUTSIDE, x=50, y=220)
		
		username_input_form = Entry(self, bd=5)
		username_input_form.place(bordermode=OUTSIDE, x=200, y=180)
		
		password_input_form = Entry(self, bd=5, show="*")
		password_input_form.place(bordermode=OUTSIDE, x=200, y=220)
		
		existingForm = Label(self, text = "Add to existing service:")
		existingForm.place(bordermode=OUTSIDE, x=50, y=265)
				
		scrollbar = Scrollbar(self, orient=VERTICAL)
		scrollbar.pack(side=RIGHT, fill=Y)
		
		add_to_existing = Listbox(self, yscrollcommand=scrollbar.set)
		add_to_existing.pack(side=LEFT, fill=BOTH)
		
		add_to_existing.config(yscrollcommand=scrollbar.set, borderwidth=4, height=2, width=21)
		scrollbar.config(command=add_to_existing.yview)
		
		add_to_existing.place(bordermode=OUTSIDE,x=200,y=260)
		scrollbar.place(x=380,y=260, height=40)
		
		def addService():
			""" This function grabs the information from the provided fields
			and adds it to the database under the user's main account. It then
			clears the fields on this frame, and redirects the user to the 
			main page.			
			"""
			username = username_input_form.get()
			password = password_input_form.get()
			servicename = service_input_form.get()
			
			print "Service:", servicename
			print "Username:", username
			print "Password:", password
			
			# ***** WHY DOESN'T THIS WORK *****
			service_page_frame = controller.getFrame(ServicesPage)
			service_page_frame.update_CurrentServices(servicename)
			#add_to_existing.insert(END, servicename)
			
			service_account = ServiceAccount(username,password,controller.current_account)

			service = Service(servicename,controller.current_account,[service_account])

			controller.current_account.service_name_list += [service]

			service.insertServiceName(controller.current_account,service)
			ServiceAccount.insertServiceAccount(controller.current_account,service,service_account)
			app.update()
			
			username_input_form.delete(0, 'end')
			password_input_form.delete(0, 'end')
			service_input_form.delete(0, 'end')
			
			controller.show_frame(ServicesPage)

		def addServiceChecker():
			""" This function checks that all the fields on this frame
			have been filled out. If a field is blank, it creates a popup
			window alerting the user to the blank field. If all fields
			are filled out, it proceeds to call addService()
			"""
			username = username_input_form.get()
			password = password_input_form.get()
			servicename = service_input_form.get()
			if (servicename) == "":
				tkMessageBox.showinfo("Error","Please enter a service name.")
			elif (username) == "":
				tkMessageBox.showinfo("Error","Please enter a valid username.")
			elif (password) == "":
				tkMessageBox.showinfo("Error","Please enter a valid password.")
			else:
				addService()
		
		add_service_button = Button(self, text ="Add Service", command=addServiceChecker)
		add_service_button.place(bordermode=OUTSIDE,x=325,y=350)
		
		more_options_button = Button(self, text ="More Options", command=lambda: controller.show_frame(ServicesPage))
		more_options_button.place(bordermode=OUTSIDE,x=200,y=350)
		
		back_button = Button(self, text ="Back", command=lambda: controller.show_frame(ServicesPage))
		back_button.place(bordermode=OUTSIDE,x=125,y=350)

if __name__ == "__main__":

	con = mdb.connect(MYSQL_LOC,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DBNAME);

	with con:
		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS FireproofAccountLogin")
		cur.execute("DROP TABLE IF EXISTS FireproofServices")
		cur.execute("DROP TABLE IF EXISTS FireproofServicesAccounts")
		cur.execute("CREATE TABLE FireproofAccountLogin (id INT(6) PRIMARY KEY,UserName VARCHAR(30) NOT NULL,\
			PasswordName VARCHAR(30) NOT NULL)")
			
	Service.createServiceTable()
	ServiceAccount.createServiceAccountsTable()
    
	app = Fireproof()
	window_width = 500
	window_height = 400
	screen_width = app.winfo_screenwidth()
	screen_height = app.winfo_screenheight()
	position_x = (screen_width/2) - (window_width/2)
	position_y = (screen_height/2) - (window_height/2)
	app.wm_geometry('%dx%d+%d+%d' % (window_width, window_height, position_x, position_y))
	app.mainloop()
