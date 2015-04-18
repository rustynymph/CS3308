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
	
	current_account = None
	
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		# the container is where we'll stack a bunch of frames
		# on top of each other, then the one we want visible
		# will be raised above the others
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

		self.show_frame(LoginPage)

	def show_frame(self, c):
		'''Show a frame for the given class'''
		frame = self.frames[c]
		frame.tkraise()


class LoginPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent) 

		username_form_label = Label(self,text="Username")
		username_form_label.place(bordermode=OUTSIDE,x=60,y=140)

		password_form_label = Label(self,text="Password")
		password_form_label.place(bordermode=OUTSIDE,x=60,y=190)
		
		username_input_form = Entry(self,bd=5)
		username_input_form.place(bordermode=OUTSIDE,x=180,y=140)

		password_input_form = Entry(self,bd=5,show="*")
		password_input_form.place(bordermode=OUTSIDE,x=180,y=190)
		
		def checkIfUser():
			is_a_user = LoginFunctions.Login(username_input_form.get(),password_input_form.get())
			if is_a_user:
				print "heyyyyyy"
				print is_a_user
				Fireproof.current_account = is_a_user
				username_input_form.delete(0, 'end')
				password_input_form.delete(0, 'end')
				controller.show_frame(ServicesPage)
		
		login_button = Button(self, text ="Login", command=checkIfUser)
		login_button.place(bordermode=OUTSIDE,x=292,y=240)		
		
		new_user_label = tk.Label(self, text="New User?", font=TEXT_FONT)
		new_user_label.place(bordermode=OUTSIDE,x=235,y=300)
		
		create_account_label = tk.Label(self, text="Click here to create an account", font=TEXT_FONT)
		create_account_label.place(bordermode=OUTSIDE,x=190,y=320)
		
		sign_up_button = Button(self, text ="Sign Up", command=lambda: controller.show_frame(CreateAccountPage))
		sign_up_button.place(bordermode=OUTSIDE,x=225,y=340)
				

class CreateAccountPage(tk.Frame):
	def __init__(self, parent, controller):
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
			LoginFunctions.createLoginInfo(username_input_form.get(),password_input_form.get(),confirm_password_input_form.get())
			controller.show_frame(LoginPage)
		
		create_account_button = Button(self, text ="Create Account", command=createAccount)
		create_account_button.place(bordermode=OUTSIDE,x=235,y=290)
		
		go_back_button = Button(self, text ="Back", command=lambda: controller.show_frame(LoginPage))
		go_back_button.place(bordermode=OUTSIDE,x=125,y=350)
		
		#tips = Label(self,text="Passwords should be at least 8 characters")
		#tips.place(bordermode=OUTSIDE,x=60,y=140)								
		
class ServicesPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)
		logout_button = Button(self, text="Logout", command=lambda: controller.show_frame(LoginPage))
		logout_button.place(bordermode=OUTSIDE,x=5,y=5)
		
		#changepassword
		change_password_button = Button(self, text="Settings", command=lambda: controller.show_frame(SettingsPage))
		change_password_button.place(bordermode=OUTSIDE,x=417,y=5)
		
		add_new_service_button = Button(self, text="Add a new service", command=lambda: controller.show_frame(AddNewServicePage))
		add_new_service_button.place(bordermode=OUTSIDE,x=355,y=365)
        
        #editpage
		edit_service_button = Button(self, text="     Edit service     ", command=lambda: controller.show_frame(EditPage))
		edit_service_button.place(bordermode=OUTSIDE,x=355,y=335)

		#deletepage
		delete_service_button = Button(self, text="    Delete service   ", command=lambda: controller.show_frame(RemoveServicePage))
		delete_service_button.place(bordermode=OUTSIDE, x=355,y=305)

class SettingsPage(tk.Frame):
	def __init__(self, parent, controller):
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
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Service Information Page", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)
        
        #editpage
		edit_service_button = Button(self, text="    Edit this service    ", command=lambda: controller.show_frame(EditPage))

		edit_service_button.place(bordermode=OUTSIDE,x=355,y=365)
		
		back_button = Button(self, text="Back", command=lambda: controller.show_frame(ServicesPage))
		back_button.place(bordermode=OUTSIDE,x=200,y=280)

class EditPage(tk.Frame):
	def __init__(self, parent, controller):
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
		tk.Frame.__init__(self, parent)
		
		existingForm = Label(self, text = "Choose a service to remove:")
		existingForm.place(bordermode=OUTSIDE, x=50, y=100)
		
		def ConfirmRemove():
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
		
		var = StringVar()
		options = OptionMenu(self, var, 'Facebook', 'Gmail', 'Moodle')
		options.pack(expand="yes", fill="x")
		var.set('Facebook')
		options.place(bordermode=OUTSIDE, x=200, y=260)
		
		def addService():
			username = username_input_form.get()
			password = password_input_form.get()
			servicename = service_input_form.get()
			print "Service:", servicename
			print "Username:", username
			print "Password:", password
			service_account = ServiceAccount(username,password)
			service = Service(servicename,[service_account])
			service.insertServiceName(Fireproof.current_account,service)
			ServiceAccount.insertServiceAccount(Fireproof.current_account,service,service_account)
			controller.show_frame(ServicesPage)

		def addServiceChecker():
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
	app.wm_geometry("500x400")
	app.mainloop()
