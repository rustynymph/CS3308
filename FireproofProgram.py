import Tkinter as tk
import tkMessageBox
from Tkinter import *
from MasterAccount import *
from FireproofFunctions import *
import MySQLdb as mdb
from config import *

TITLE_FONT = ("Helvetica", 18, "bold")
class Fireproof(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		# the container is where we'll stack a bunch of frames
		# on top of each other, then the one we want visible
		# will be raised above the others
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}
		for F in (StartPage, LoginPage, CreateAccountPage, ServicesPage, ServiceInfoPage):
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

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent) 
		label = tk.Label(self, text="This is the start page", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)
		
		logo = PhotoImage(file="fireproof.png")
		w1 = Label(image=logo)
		w1.image = logo
		w1.place(bordermode=OUTSIDE,x=150,y=15)
				

		button1 = tk.Button(self, text="Go to Page One", 
							command=lambda: controller.show_frame(LoginPage))
		button1.place(bordermode=OUTSIDE,x=180,y=140)
		button2 = tk.Button(self, text="Go to Page Two",
							command=lambda: controller.show_frame(CreateAccountPage))
		button2.place(bordermode=OUTSIDE,x=180,y=340)



class LoginPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent) 
		#label = tk.Label(self, text="This is the login page", font=TITLE_FONT)
		#label.pack(side="top", fill="x", pady=10)
		#button = tk.Button(self, text="Go to the main page", 
		#				   command=lambda: controller.show_frame(StartPage))
						   				   
		#button.pack()
		userForm = Label(self,text="Username")
		userForm.place(bordermode=OUTSIDE,x=60,y=140)

		passForm = Label(self,text="Password")
		passForm.place(bordermode=OUTSIDE,x=60,y=190)

		userVar = Entry(self,bd=5)
		userVar.place(bordermode=OUTSIDE,x=180,y=140)

		passVar = Entry(self,bd=5,show="*")
		passVar.place(bordermode=OUTSIDE,x=180,y=190)
		
		Enter = Button(self, text ="Login", command=lambda: FireproofFunctions.Login(userVar.get(),passVar.get()))
		Enter.place(bordermode=OUTSIDE,x=160,y=240)		
		
		Enter = Button(self, text ="Create Account", command=lambda: controller.show_frame(CreateAccountPage))
		Enter.place(bordermode=OUTSIDE,x=235,y=240)			

class CreateAccountPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		#label = tk.Label(self, text="This is create account page", font=TITLE_FONT)
		#label.pack(side="top", fill="x", pady=10)
		#button = tk.Button(self, text="Go to the main page", 
						  # command=lambda: controller.show_frame(StartPage))
		#button.pack()
		
		userForm = Label(self,text="Create Username")
		userForm.place(bordermode=OUTSIDE,x=60,y=140)

		passForm = Label(self,text="Create Password")
		passForm.place(bordermode=OUTSIDE,x=60,y=190)
		
		confirmPassForm = Label(self,text="Confirm Password")
		confirmPassForm.place(bordermode=OUTSIDE,x=60,y=240)

		userVar = Entry(self,bd=5)
		userVar.place(bordermode=OUTSIDE,x=180,y=140)

		passVar = Entry(self,bd=5,show="*")
		passVar.place(bordermode=OUTSIDE,x=180,y=190)
		
		confirmPassVar = Entry(self,bd=5,show="*")
		confirmPassVar.place(bordermode=OUTSIDE,x=180,y=240)
		
		Enter = Button(self, text ="Create Account", command=lambda: FireproofFunctions.createLoginInfo(userVar.get(),passVar.get()))
		Enter.place(bordermode=OUTSIDE,x=235,y=290)							
		
class ServicesPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)
		button = tk.Button(self, text="Go to the start page", 
						   command=lambda: controller.show_frame(StartPage))
		button.pack()
		
class ServiceInfoPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)
		button = tk.Button(self, text="Go to the start page", 
						   command=lambda: controller.show_frame(StartPage))
		button.pack()		

if __name__ == "__main__":
	app = Fireproof()
	app.wm_geometry("500x400")
	app.mainloop()