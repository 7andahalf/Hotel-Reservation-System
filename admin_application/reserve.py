#!/usr/bin/python
from Tkinter import *
import tkMessageBox,Tkinter,comm
import util

# The main window which shows all the hotels with that particular facility
class book(util.window):
	# Name of the thing is required like room, banquet etc
	def __init__(self, server, name):
		self.server = server
		self.name = name

		if not server.testConnection():
			tkMessageBox.showerror("Connection Failed", "Connection to the server failed please try again later.")
			self.root.destroy()
		udata = server.req('get_user_details')
		hotels = server.req('get_all_hotels')

		# create window and its widgets
		util.window.__init__(self,"SVS HOTELS | Computerized Reservation System | Make a reservation")

		canvas = Canvas(width = 600, height = 150, bg = 'white')
		canvas.pack(expand = YES, fill = BOTH)
		gif1 = PhotoImage(file = './data/3.gif')
		canvas.create_image(0, 0, image = gif1, anchor = NW)

		user_frame = Frame(self.root, height = 40, width = 580, relief = RAISED, bd = 1)
		user_frame.place(x=10,y=165)

		logout_button = Button(user_frame, text ="back", command=(lambda: self.root.destroy()))
		logout_button.place(x=330+180, y = 2)

		x,y = 10,6

		label_info = Label(user_frame, text="Pick a hotel to reserve " + name)
		label_info.place(x=x, y = y)

		main_frame = Frame(self.root, height = 260, width = 580, relief = RAISED, bd = 0)
		main_frame.place(x=10,y=215)

		def data():
			j = 0
			for i in hotels:
				if len(i[name]) > 0:
					subFrame = Frame(frame, height = 40, width = 550, relief = RAISED, bd = 1)
					subFrame.grid(row=j,column=0)
					Label(subFrame,text=str(j+1)+".").place(x=5,y=7)
					Label(subFrame,text=i['name']).place(x=30,y=7)
					Button(subFrame, text ="Choose", command=book2(server,i,name,self).show).place(x=470,y=4)
					j+=1

		def myfunction(event):
		    canvas.configure(scrollregion=canvas.bbox("all"),width=557,height=260)

		# Creates a scrollable frame so that many results can be displayed there
		canvas=Canvas(main_frame)
		frame=Frame(canvas)
		myscrollbar=Scrollbar(main_frame,orient="vertical",command=canvas.yview)
		canvas.configure(yscrollcommand=myscrollbar.set)

		myscrollbar.pack(side="right",fill="y")
		canvas.pack(side="left")
		canvas.create_window((0,0),window=frame,anchor='nw')
		frame.bind("<Configure>",myfunction)
		data()

		self.root.mainloop()

# This window shows variations of the same type in a particular hotel
class book2(util.window):
	def __init__(self,server,hotel,name,main):
		self.server = server
		self.hotel = hotel
		self.name = name
		self.main = main
	def show(self):
			dat = self.hotel
			name = self.name
			server = self.server

			# create window and its widgets
			util.window.__init__(self,"SVS HOTELS | " + dat['name'] + " | " + name)
			root = self.root

			user_frame = Frame(root, height = 40, width = 580, relief = RAISED, bd = 1)
			user_frame.place(x=10,y=10)

			logout_button = Button(user_frame, text ="back", command=(lambda: root.destroy()))
			logout_button.place(x=330+180, y = 2)

			x,y = 10,6

			label_info = Label(user_frame, text="Book " + name + " in the hotel: "  + dat['name'])
			label_info.place(x=x, y = y)

			main_frameH = Frame(root, height = 400, width = 580, relief = RAISED, bd = 0)
			main_frameH.place(x=10,y=60)

			def components():
				j = 0

				subFrame = Frame(Hframe, height=40, width = 550, relief = RAISED, bd = 0)
				subFrame.grid(row=j,column=0)
				Label(subFrame,text='Following are available for booking:', font=("helvetica", 19)).place(x=5,y=7)
				j+=1

				for i in dat[name]:
					subFrame = Frame(Hframe, height = 40, width = 550, relief = RAISED, bd = 0)
					subFrame.grid(row=j,column=0)
					Label(subFrame,text=i['name'], font=("helvetica", 16)).place(x=30,y=7)
					Button(subFrame, text ="Choose", command=book3(server,dat,name,i,self.main,self).show).place(x=470,y=4)
					Label(Hframe,text="\t"+i['description'],wraplength=540,justify=LEFT).grid(row=j+1,column=0)
					j+=2

			def myfunctionH(event):
			    Hcanvas.configure(scrollregion=Hcanvas.bbox("all"),width=557,height=400)

			Hcanvas=Canvas(main_frameH)
			Hframe=Frame(Hcanvas)
			myscrollbarH=Scrollbar(main_frameH,orient="vertical",command=Hcanvas.yview)
			Hcanvas.configure(yscrollcommand=myscrollbarH.set)

			myscrollbarH.pack(side="right",fill="y")
			Hcanvas.pack(side="left")
			Hcanvas.create_window((0,0),window=Hframe,anchor='nw')
			Hframe.bind("<Configure>",myfunctionH)
			components()

			root.mainloop()

# Creates an object for button to work with
class book3(util.window):
	def __init__(self,server,hotel,name,dat,main,main2):
		self.server = server
		self.hotel = hotel
		self.dat = dat
		self.name = name
		self.main = main
		self.main2 = main2
	def show(self):
		if self.name == 'restaurants':
			bookrest(self.server, self.hotel, self.dat, self.main, self.main2).show()
		else:
			bookRoomsBanqMeeting(self.server, self.hotel, self.dat, self.main, self.main2, self.name).show()


# This window is used to book Rooms - Banquet - Meeting rooms
class bookRoomsBanqMeeting(util.window):
	def __init__(self,server,hotel,dat,main,main2, name):
		self.server = server
		self.hotel = hotel
		self.dat = dat
		self.name = name
		self.main = main
		self.main2 = main2
	def show(self):
			dat = self.hotel
			server = self.server
			name = self.name
			thing = self.dat
			util.window.__init__(self,"SVS HOTELS | " + dat['name'] + " | " + name)
			root = self.root

			def check():
				if not server.testConnection():
					tkMessageBox.showerror("Connection Failed", "Connection to the server failed please try again later.",parent=root)
					self.main.root.destroy()

				fine = True

				# Various checks to verify the user inputs
				def greaterDate(one,two):
				        if int(one[2]) > int(two[2]):return True
				        elif int(one[2]) < int(two[2]): return False
				        if int(one[1]) > int(two[1]):return True
				        elif int(one[1]) < int(two[1]): return False
				        if int(one[0]) > int(two[0]):return True
				        elif int(one[0]) < int(two[0]): return False
				        if int(one[3]) > int(two[3]):return True
				        elif int(one[3]) < int(two[3]): return False
				        if int(one[4]) > int(two[4]):return True
				        elif int(one[4]) < int(two[4]): return False
				        if int(one[5]) > int(two[5]):return True
				        elif int(one[5]) <= int(two[5]): return False

				try:
					fro = [int(i) for i in entry_from.get().split(".")]
					to = [int(i) for i in entry_to.get().split(".")]
					if self.name == 'rooms':
						qty = int(entry_qty.get())
						if not greaterDate(to, fro):
							raise Exception
					else:
						qty = 1
					if len(fro) < 3 or len(to) < 3 or qty < 1:
						raise Exception
					d,m,y = fro
					if not (type(d) is int and type(m) is int and type(y) is int and
						    y > 0 and (0 < m <= 12) and
						      (  ((m in [1,3,5,7,8,10,12]) and (0<d<=31)) or
							 ((m in [4,6,9,11]) and (0<d<=30)) or
							 ((m == 2) and ((0 < d <= 28 and y % 4 != 0) or (0 < d <= 29 and y % 4 == 0)))
						      )):
						raise Exception
					d,m,y = to
					if not (type(d) is int and type(m) is int and type(y) is int and
						    y > 0 and (0 < m <= 12) and
						      (  ((m in [1,3,5,7,8,10,12]) and (0<d<=31)) or
							 ((m in [4,6,9,11]) and (0<d<=30)) or
							 ((m == 2) and ((0 < d <= 28 and y % 4 != 0) or (0 < d <= 29 and y % 4 == 0)))
						      )):
						raise Exception
					d = str(entry_comment.get())
				except:
					tkMessageBox.showerror("Invalid entry", "Please enter numbers according to the format provided into fields",parent=root)
					fine = False

				# do this only if everything is fine
				if fine:
					fro = [int(i) for i in entry_from.get().split(".")]
					to = [int(i) for i in entry_to.get().split(".")]
					totime = [0,0,0]
					if self.name == 'rooms':
						qty = int(entry_qty.get())
					else:
						qty = 1
						totime[0]=23
						totime[1]=59
						totime[2]=59

					# check availability and prompt to book
					data = server.req('availability',dat['id'],name,thing['id'],fro[0],fro[1],fro[2],0,0,0,to[0],to[1],to[2],totime[0],totime[1],totime[2])[0]
					if qty > data:
						tkMessageBox.showerror("Unavaialable", "Sorry these many quantites are not available. Only " +str(data)+ " are available.",parent=root)
					else:
						if tkMessageBox.askyesno("Availability", "The required quantity are available. Do you want to confirm booking?",parent=root):
							data = server.req('make_reservation',dat['id'],name,thing['id'],fro[0],fro[1],fro[2],0,0,0,to[0],to[1],to[2],0,0,0,str(entry_comment.get()),"",qty,"","")
							if data:
								tkMessageBox.showinfo("Successfully booked", "Successfully reserved the required quantity. Our representative will speak with you within 24 hrs. to confirm the booking and payment method.",parent=root)
								self.root.destroy()
								self.main2.root.destroy()
								self.main.root.destroy()

			user_frame = Frame(root, height = 40, width = 580, relief = RAISED, bd = 1)
			user_frame.place(x=10,y=10)

			logout_button = Button(user_frame, text ="back", command=(lambda: root.destroy()))
			logout_button.place(x=330+180, y = 2)

			x,y = 10,6

			label_info = Label(user_frame, text="Book " + name + " in the hotel: "  + dat['name'])
			label_info.place(x=x, y = y)

			main_frameH = Frame(root, height = 400, width = 580, relief = RAISED, bd = 0)
			main_frameH.place(x=10,y=60)

			main_frame = Frame(root, height = 400, width = 580, relief = RAISED, bd = 1)
			main_frame.place(x=10,y=60)

			x,y = 10,6

			label_info = Label(main_frame, text=thing['name'])
			label_info.place(x=x, y = y)

			try:
				label_info = Label(main_frame, text="Price per day: " + str(thing['price']))
				label_info.place(x=x+400-80, y = y)
			except:
				pass

			label_info = Label(main_frame, text="Booking information: ")
			label_info.place(x=x, y = y+30)

			x,y = 80,6-80

			label_info = Label(main_frame, text="From Date (DD.MM.YYYY) : ")
			label_info.place(x=x, y = y+140)

			entry_from = Entry(main_frame)
			entry_from.place(x=x+200, y = y+140)

			label_info = Label(main_frame, text="To Date (DD.MM.YYYY) : ")
			label_info.place(x=x, y = y+170)

			entry_to = Entry(main_frame)
			entry_to.place(x=x+200, y = y+170)

			if self.name == 'rooms':
				label_qty = Label(main_frame, text="Quantity : ")
				label_qty.place(x=x, y = y+200)

				entry_qty = Entry(main_frame)
				entry_qty.place(x=x+200, y = y+200)
			else:
				label_qty = Label(main_frame, text="Put the same date if you want to book only one day")
				label_qty.place(x=x, y = y+200)

			label_qty = Label(main_frame, text="Flight Details, Comments and Special Requests: ")
			label_qty.place(x=x, y = y+230)

			entry_comment = Entry(main_frame, width=37)
			entry_comment.place(x=x+50, y = y+260)

			check_button = Button(main_frame, text ="Check availability", command=check)
			check_button.place(x=200, y = 240)

			root.mainloop()

# This window is used to book Restaurants
class bookrest(util.window):
	def __init__(self,server,hotel,dat,main,main2):
		self.server = server
		self.hotel = hotel
		self.dat = dat
		self.name = 'restaurants'
		self.main = main
		self.main2 = main2
	def show(self):
			dat = self.hotel
			server = self.server
			name = self.name
			thing = self.dat
			util.window.__init__(self,"SVS HOTELS | " + dat['name'] + " | " + name)
			root = self.root

			# By: Vinay C K
			def check():
				if not server.testConnection():
					tkMessageBox.showerror("Connection Failed", "Connection to the server failed please try again later.",parent=root)
					self.main.root.destroy()

				fine = True

				# Various checks to verify the user inputs
				try:
					date = [int(i) for i in entry_from.get().split(".")]
					time = [int(i) for i in entry_to.get().split(":")]
					qty = int(entry_qty.get())
					if len(date) < 3 or len(time) < 2 or qty < 1:
						raise Exception
					d,m,y = date
					if not (type(d) is int and type(m) is int and type(y) is int and
						    y > 0 and (0 < m <= 12) and
						      (  ((m in [1,3,5,7,8,10,12]) and (0<d<=31)) or
							 ((m in [4,6,9,11]) and (0<d<=30)) or
							 ((m == 2) and ((0 < d <= 28 and y % 4 != 0) or (0 < d <= 29 and y % 4 == 0)))
						      )):
						raise Exception
					h,m = time
					if not (0 <= h < 24 and 0 <= m < 60):
						raise Exception
					d = str(entry_comment.get())
				except:
					tkMessageBox.showerror("Invalid entry", "Please enter numbers according to the format provided into fields",parent=root)
					fine = False
				if fine:
					date = [int(i) for i in entry_from.get().split(".")]
					time = [int(i) for i in entry_to.get().split(":")]
					qty = int(entry_qty.get())

					time2, date2 = time[:], date[:]
					if (time[0] + 2) >= 24:
						time2[0] = time[0] - 22
						date2[0] = date[0] + 1

						if ((date2[1] in [1,3,5,7,8,10,12] and date2[0] > 31) or
						    (date2[1] in [4,6,9,11] and date2[0] > 30) or
						    ((date2[1] == 2) and (date2[0] > 28 and date[2] % 4 != 0) or 
									   (date2[0] > 29 and date[2] % 4 == 0 ))
							):
							date2[0] = 1
							date2[1] = date[1] + 1
							if date2[1] > 12:
								date2[1] = 1
								date2[2] = date[2] + 1
					else:
						time2[0] = time[0] + 2

					data = server.req('availability',dat['id'],name,thing['id'],date[0],date[1],date[2],time[0],time[1],0,date2[0],date2[1],date2[2],time2[0],time2[1],0)[0]
					if qty > data:
						tkMessageBox.showerror("Unavaialable", "Sorry these many quantites are not available. Only " +str(data)+ " are available.",parent=root)
					else:
						if tkMessageBox.askyesno("Availability", "The required quantity are available. Do you want to confirm booking?",parent=root):
							data = server.req('make_reservation',dat['id'],name,thing['id'],date[0],date[1],date[2],time[0],time[1],0,date2[0],date2[1],date2[2],time2[0],time2[1],0,str(entry_comment.get()),"",qty,"","")
							if data:
								tkMessageBox.showinfo("Successfully booked", "Successfully reserved the required quantity. Our representative will speak with you within 24 hrs. to confirm the booking and payment method.",parent=root)
								self.root.destroy()
								self.main2.root.destroy()
								self.main.root.destroy()
								

			user_frame = Frame(root, height = 40, width = 580, relief = RAISED, bd = 1)
			user_frame.place(x=10,y=10)

			logout_button = Button(user_frame, text ="back", command=(lambda: root.destroy()))
			logout_button.place(x=330+180, y = 2)

			x,y = 10,6

			label_info = Label(user_frame, text="Book " + name + " in the hotel: "  + dat['name'])
			label_info.place(x=x, y = y)

			main_frameH = Frame(root, height = 400, width = 580, relief = RAISED, bd = 0)
			main_frameH.place(x=10,y=60)

			main_frame = Frame(root, height = 400, width = 580, relief = RAISED, bd = 1)
			main_frame.place(x=10,y=60)

			x,y = 10,6

			label_info = Label(main_frame, text=thing['name'])
			label_info.place(x=x, y = y)

			try:
				label_info = Label(main_frame, text="Price per day: " + str(thing['price']))
				label_info.place(x=x+400-80, y = y)
			except:
				pass

			label_info = Label(main_frame, text="Booking information: ")
			label_info.place(x=x, y = y+30)

			x,y = 80,6-80

			label_info = Label(main_frame, text="Date (DD.MM.YYYY): ")
			label_info.place(x=x, y = y+140)

			entry_from = Entry(main_frame)
			entry_from.place(x=x+200, y = y+140)

			label_info = Label(main_frame, text="Time (HH:MM 24 Hr format): ")
			label_info.place(x=x, y = y+170)

			entry_to = Entry(main_frame)
			entry_to.place(x=x+200, y = y+170)

			label_qty = Label(main_frame, text="Number of people : ")
			label_qty.place(x=x, y = y+200)

			entry_qty = Entry(main_frame)
			entry_qty.place(x=x+200, y = y+200)

			label_qty = Label(main_frame, text="Comments and Special Requests: ")
			label_qty.place(x=x, y = y+230)

			entry_comment = Entry(main_frame, width=37)
			entry_comment.place(x=x+50, y = y+260)

			check_button = Button(main_frame, text ="Check availability", command=check)
			check_button.place(x=200, y = 240)

			root.mainloop()
if __name__ == "__main__":
	server = comm.link('vinay','letmein')
	server.login()
	book(server,'restaurants')
