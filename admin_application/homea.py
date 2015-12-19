#!/usr/bin/python
from Tkinter import *
import tkMessageBox,Tkinter,comm
import util

class home(util.window):
	def __init__(self, server):
		self.server = server

		# Functions to be called on button clicks
		def viewHotels():
			self.status['home'] = 'viewhotels'
			self.root.destroy()
		def reserve(name):
			self.status['home'] = 'reserve'
			self.reser = name
			self.root.destroy()
		def viewBookings():
			self.status['home'] = 'viewbooking'
			self.root.destroy()
		def aboutus():
			self.status['home'] = 'aboutus'
			self.root.destroy()
		def contactus():
			self.status['home'] = 'contactus'
			self.root.destroy()
		def viewRes():
			self.status['home'] = 'viewres'
			self.root.destroy()
		def viewRes2():
			self.status['home'] = 'viewres2'
			self.root.destroy()
		def viewUsers():
			self.status['home'] = 'viewusers'
			self.root.destroy()

		# Test server connection
		if not server.testConnection():
			tkMessageBox.showerror("Connection Failed", "Connection to the server failed please try again later.")
			self.root.destroy()

		# fetch data of user
		udata = server.req('get_user_details')

		# Init
		util.window.__init__(self,"SVS HOTELS | Computerized Reservation System | Home")

		# Top image
		canvas = Canvas(width = 600, height = 150, bg = 'white')
		canvas.pack(expand = YES, fill = BOTH)
		gif1 = PhotoImage(file = './data/3.gif')
		canvas.create_image(0, 0, image = gif1, anchor = NW)

		# top bar frame
		user_frame = Frame(self.root, height = 40, width = 580, relief = RAISED, bd = 1)
		user_frame.place(x=10,y=165)

		x,y = 10,6

		label_info = Label(user_frame, text="Welcome "+ udata['name'])
		label_info.place(x=x, y = y)

		logout_button = Button(user_frame, text ="logout", command=(lambda: self.root.destroy()))
		logout_button.place(x=x+330+160, y = y-2)

		# reservation rooms
		x,y = 20,20

		reserv_frame = Frame(self.root, height = 100, width = 200, relief = RAISED, bd = 1)
		reserv_frame.place(x=10,y=215)

		label_reserv = Label(reserv_frame, text="Reservation for rooms")
		label_reserv.place(x=x+5, y = y+0)

		reserv_button = Button(reserv_frame, text ="Book rooms", command=(lambda: reserve('rooms')))
		reserv_button.place(x=x+30, y = y+25)


		# Reserve restaurants
		x,y = 20,20

		restresrv_frame = Frame(self.root, height = 100, width = 200, relief = RAISED, bd = 1)
		restresrv_frame.place(x=10,y=325)

		label_restresrv = Label(restresrv_frame, text="Reservation for restaurants")
		label_restresrv.place(x=x-9, y = y+0)

		restresrv_button = Button(restresrv_frame, text ="Book restaurants", command=(lambda: reserve('restaurants')))
		restresrv_button.place(x=x+10, y = y+25)

		# Reserve banquet halls
		x,y = 20,20

		registerban_frame = Frame(self.root, height = 100, width = 200, relief = RAISED, bd = 1)
		registerban_frame.place(x=230,y=215)

		label_ban = Label(registerban_frame, text="Banquet hall reservations")
		label_ban.place(x=x-9, y = y+0)

		ban_button = Button(registerban_frame, text ="Book banquet halls", command=(lambda: reserve('banquet')))
		ban_button.place(x=x+5, y = y+25)

		# side bar
		x,y = 20,20

		registermeet_frame = Frame(self.root, height = 260, width = 140, relief = RAISED, bd = 1)
		registermeet_frame.place(x=450,y=215)


		register_meet = Button(registermeet_frame, text ="Reservations",width = 10, command=(lambda: viewRes()))
		register_meet.place(x=x-10, y = y-15)

		register_meet = Button(registermeet_frame, text ="Ad.Reservation",width = 10, command=(lambda: viewRes2()))
		register_meet.place(x=x-10, y = y+15)

		register_meet = Button(registermeet_frame, text ="View Users",width = 10, command=(lambda: viewUsers()))
		register_meet.place(x=x-10, y = y+45)

		x,y = x,y+90
		
		register_meet = Button(registermeet_frame, text ="View all hotels", command=(lambda: viewHotels()))
		register_meet.place(x=x-10, y = y-15)

		register_meet = Button(registermeet_frame, text ="About Us",width = 10, command=(lambda: aboutus()))
		register_meet.place(x=x-10, y = y+15)

		register_meet = Button(registermeet_frame, text ="Contact Us",width = 10, command=(lambda: contactus()))
		register_meet.place(x=x-10, y = y+45)



		# reserve meeting rooms
		x,y = 20,20

		registermeet_frame = Frame(self.root, height = 100, width = 200, relief = RAISED, bd = 1)
		registermeet_frame.place(x=230,y=325)

		label_meet = Label(registermeet_frame, text="Meeting room reservations")
		label_meet.place(x=x-9, y = y+0)

		register_meet = Button(registermeet_frame, text ="Book meeting rooms", command=(lambda: reserve('meeting')))
		register_meet.place(x=x, y = y+25)

		# past reservations
		user_frame = Frame(self.root, height = 40, width = 420, relief = RAISED, bd = 1)
		user_frame.place(x=10,y=435)

		x,y = 10,6

		label_infovp = Label(user_frame, text="View your previous reservations")
		label_infovp.place(x=x, y = y)

		logout_buttonvp = Button(user_frame, text ="View past bookings", command=viewBookings)
		logout_buttonvp.place(x=x+240, y = y-2)

		self.status['home'] = 'active'

		# run
		self.root.mainloop()

if __name__ == "__main__":
	server = comm.link('vinay','letmein')
	server.mode = 'a'
	server.login()
	home(server)