#!/usr/bin/python
from Tkinter import *
import tkMessageBox,Tkinter,comm
import util

class login(util.window):
	def __init__(self):
		
		# Init
		util.window.__init__(self,"SVS HOTELS | Computerized Reservation System | LOGIN")

		# Top image
		canvas = Canvas(self.root,width = 600, height = 150, bg = 'white')
		canvas.pack(expand = YES, fill = BOTH)
		gif1 = PhotoImage(file = './data/3.gif')
		canvas.create_image(0, 0, image = gif1, anchor = NW)

		# Login frame
		login_frame = Frame(self.root, height = 175, width = 420, relief = FLAT, bd = 1)
		login_frame.place(x=80,y=175)

		x,y = 70,20

		Label(login_frame, text="Please enter your details to login").place(x=x+30, y = y+0)

		Label(login_frame, text="Username: ").place(x=x+0, y = y+30)
		Label(login_frame, text="Password: ").place(x=x+0, y = y+60)

		entry_usern = Entry(login_frame)
		entry_passw = Entry(login_frame, show="*")
		entry_usern.place(x=x+80, y = y+30)
		entry_passw.place(x=x+80, y = y+60)

		mode = StringVar(login_frame)
		mode.set("Admin")
 		label_mode = Label(login_frame, text="Login As: ")
		label_mode.place(x=x, y = y+90)
		pick_mode = OptionMenu(login_frame,mode, "User","Admin")
		pick_mode.place(x=x+80, y = y+90)

		Button(login_frame, text ="Login", command=(lambda: self.loginCheck(entry_usern.get(),entry_passw.get(),mode.get()))).place(x=x+80, y = y+120)

		# Forgot pass
		x,y = 20,20

		forgotpass_frame = Frame(self.root, height = 100, width = 200, relief = RAISED, bd = 1)
		forgotpass_frame.place(x=80,y=360)

		Label(forgotpass_frame, text="Forgot your password?").place(x=x+6, y = y+0)

		forgotpass_button = Button(forgotpass_frame, text ="Recover password", command=(lambda: self.forgotPass()))
		forgotpass_button.place(x=x+10, y = y+25)

		# Register
		x,y = 20,20

		register_frame = Frame(self.root, height = 100, width = 200, relief = RAISED, bd = 1)
		register_frame.place(x=300,y=360)

		Label(register_frame, text="New user?").place(x=x+43, y = y+0)

		register_button = Button(register_frame, text ="Register", command=(lambda: self.registerUser()))
		register_button.place(x=x+40, y = y+25)

		self.status['login'] = 'active'

		# run
		self.root.mainloop()
	
	def forgotPass(self):
		self.status['login'] = 'forgotpass'
		self.root.destroy()

	def registerUser(self):
		self.status['login'] = 'register'
		self.root.destroy()

	def loginCheck(self, usern, passw, mode):
		if mode == 'User':
			server = comm.link(usern,passw)
			server.mode = 'u'
			if not comm.link.testConnection():
				tkMessageBox.showerror("Connection Failed", "Connection to the server failed please try again later.")

			try:
				server.login()
				self.server = server
				self.status['login'] = 'passu'
				self.root.destroy()
			except:
				tkMessageBox.showerror("Authentication Failed", "Invalid combination of username and password.")
		else:
			server = comm.link(usern,passw)
			server.mode = 'a'
			if not comm.link.testConnection():
				tkMessageBox.showerror("Connection Failed", "Connection to the server failed please try again later.")

			try:
				server.login()
				self.server = server
				self.status['login'] = 'passa'
				self.root.destroy()
			except:
				tkMessageBox.showerror("Authentication Failed", "Invalid combination of username and password.")



if __name__ == "__main__":
	login()