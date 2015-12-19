#!/usr/bin/python
from Tkinter import *
import tkMessageBox,Tkinter,comm
import util

# Provides options to select a reservation
class viewRes(util.window):
	def __init__(self, server):
		if not server.testConnection():
			tkMessageBox.showerror("Connection Failed", "Connection to the server failed please try again later.")
			self.root.destroy()
		udata = server.req('get_user_details')
		hotels = server.req('get_all_hotels')

		util.window.__init__(self,"SVS HOTELS | Computerized Reservation System | View Reservations")

		canvas = Canvas(width = 600, height = 150, bg = 'white')
		canvas.pack(expand = YES, fill = BOTH)
		gif1 = PhotoImage(file = './data/3.gif')
		canvas.create_image(0, 0, image = gif1, anchor = NW)

		user_frame = Frame(self.root, height = 40, width = 580, relief = RAISED, bd = 1)
		user_frame.place(x=10,y=165)

		logout_button = Button(user_frame, text ="back", command=(lambda: self.root.destroy()))
		logout_button.place(x=330+180, y = 2)

		x,y = 10,6

		label_info = Label(user_frame, text="View Reservations")
		label_info.place(x=x, y = y)

		main_frame = Frame(self.root, height = 260, width = 580, relief = RAISED, bd = 0)
		main_frame.place(x=10,y=215)

		label_info = Label(main_frame, text="Select options to view reservations")
		label_info.place(x=x+100, y = y+10)

		x, y = 100, 100
		thing_frame = Frame(main_frame, height = 40, width = 500, relief = RAISED, bd = 0)
		thingT_frame = Frame(main_frame, height = 40, width = 500, relief = RAISED, bd = 0)
		variableTT = StringVar(thingT_frame)
		variableT = StringVar(thing_frame)

		def viewRes():
			h,t,tt = variable.get(),'',''
			if h != '':
				t = variableT.get()
				if t != '':
					tt = variableTT.get()
			view(h,t,tt,server)

		def hotelVar(*args):
			def thingVar(*args):
				if variableT.get() == '':
					pass
				else:
					thingT_frame.place(x=x+10,y=100)
					label_info = Label(thingT_frame, text="Pick a type")
					label_info.place(x=0, y = 3)
					variableTT.set("") # default value
					thingT = apply(OptionMenu, (thingT_frame, variableTT) + tuple([i['name'] for i in partHotel[variableT.get()]]))
					thingT.place(x = 100, y= 0)
			if variable.get() == '':
				pass
			else:
				thing_frame.place(x=x+10,y=70)
				label_info = Label(thing_frame, text="Pick a type")
				label_info.place(x=0, y = 3)
				things = ['rooms', 'restaurants', 'banquet', 'meeting']
				for i in hotels:
					if i['name'] == variable.get():
						partHotel = i
				variableT.trace("w", thingVar)
				variableT.set("") # default value
				thing = apply(OptionMenu, (thing_frame, variableT) + tuple([i for i in things if len(partHotel[i]) > 0]))
				thing.place(x = 100, y= 0)

		hotel_frame = Frame(main_frame, height = 30, width = 500, relief = RAISED, bd = 0)
		hotel_frame.place(x=x+10,y=40)

		label_info = Label(hotel_frame, text="Pick a hotel")
		label_info.place(x=0, y = 3)

		variable = StringVar(hotel_frame)
		variable.set([i['name'] for i in hotels][0]) 
		variable.trace("w", hotelVar)
		hot = apply(OptionMenu, (hotel_frame, variable) + tuple([i['name'] for i in hotels]))
		hot.place(x = 100, y= 0)

		view_button = Button(main_frame, text ="View Reservations", command=(lambda: viewRes()))
		view_button.place(x=200, y = 150)

		self.root.mainloop()

# Views the reservations that are in the given criteria
class view(util.window):
	def __init__(self,h,t,tt,server):
			self.h = h
			self.t = t
			self.tt = tt
			self.server = server
			hotels = server.req('get_all_hotels')
			util.window.__init__(self,"SVS HOTELS | View reservation", width = 700)

			root = self.root

			user_frame = Frame(root, height = 40, width = 680, relief = RAISED, bd = 1)
			user_frame.place(x=10,y=10)

			logout_button = Button(user_frame, text ="back", command=(lambda: root.destroy()))
			logout_button.place(x=330+280, y = 2)

			x,y = 10,6

			label_info = Label(user_frame, text="View reservation")
			label_info.place(x=x, y = y)

			self.populate()
			root.mainloop()

	def populate(self):
			h = self.h
			t = self.t
			tt = self.tt
			root = self.root
			server = self.server
			hotels = server.req('get_all_hotels')
			main_frameH = Frame(root, height = 400, width = 680, relief = RAISED, bd = 0)
			main_frameH.place(x=10,y=60)
			self.mainfr = main_frameH

			for i in hotels:
					if i['name'] == h:
						ih = i['id']
						tts = i
			if t == '':
				data = server.req('get_allbookings_of',ih)
			elif tt == '':
				data = server.req('get_allbookings_of',ih,t)
			else:
				for i in tts[t]:
					if i['name'] == tt:
						itt = i['id']
				data = server.req('get_allbookings_of',ih,t,itt)

			def components():
				j = 0
				subframe = Frame(Hframe, width = 680, height = 30, bd = 1)
				subframe.grid(row=j,column=0)
				Label(subframe,text="ID").place(x=0,y=0)
				Label(subframe,text="By").place(x=20,y=0)
				Label(subframe,text="What").place(x=50,y=0)
				Label(subframe,text="Qty").place(x=170,y=0)
				Label(subframe,text="Status").place(x=210,y=0)
				Label(subframe,text="From").place(x=270,y=0)
				Label(subframe,text="To").place(x=400,y=0)
				Label(subframe,text="Action").place(x=570,y=0)
				j+=1
				for i in data:
					subframe = Frame(Hframe, width = 680, height = 30)
					subframe.grid(row=j,column=0)
					Label(subframe,text=i['id']).place(x=0,y=0)
					Label(subframe,text=i['by'][0]+':'+i['by'][1]).place(x=20,y=0)
					Label(subframe,text=i['what'][0]+":"+i['what'][1]+":"+i['what'][2]).place(x=50,y=0)
					Label(subframe,text=i['quantity']).place(x=170,y=0)
					Label(subframe,text=i['confirmed']).place(x=210,y=0)
					Label(subframe,text="".join([":"+k for k in i['from'][:3]])[1:]).place(x=270,y=0)
					Label(subframe,text="".join([":"+k for k in i['from'][3:]])[1:]).place(x=350,y=0)
					Label(subframe,text="".join([":"+k for k in i['to'][:3]])[1:]).place(x=400,y=0)
					Label(subframe,text="".join([":"+k for k in i['to'][3:]])[1:]).place(x=480,y=0)
					Button(subframe,text="View", command = view2(i,server,self).show).place(x=570,y=-3)
					j+=1

			def myfunctionH(event):
			    Hcanvas.configure(scrollregion=Hcanvas.bbox("all"),width=657,height=400)
			Hcanvas=Canvas(main_frameH)
			Hframe=Frame(Hcanvas)
			myscrollbarH=Scrollbar(main_frameH,orient="vertical",command=Hcanvas.yview)
			Hcanvas.configure(yscrollcommand=myscrollbarH.set)

			myscrollbarH.pack(side="right",fill="y")
			Hcanvas.pack(side="left")
			Hcanvas.create_window((0,0),window=Hframe,anchor='nw')
			Hframe.bind("<Configure>",myfunctionH)
			components()

	def reload(self):
		self.mainfr.destroy()
		self.populate()

# Views a particular reservation
class view2(util.window):
	def __init__(self,res,server,main):
		self.dat = res
		self.server = server
		self.main = main
	def show(self):
			server = self.server
			def commCon():
				dat = server.req('mark_reservation',self.dat['id'],'confirm')
				tkMessageBox.showinfo('Marked Reservation', 'Reservation successfully confirmed', parent = root)
				self.root.destroy()
				self.main.reload()
			def commCan():
				dat = server.req('mark_reservation',self.dat['id'],'cancel')
				tkMessageBox.showinfo('Marked Reservation', 'Reservation cancelled.', parent = root)
				self.root.destroy()
				self.main.reload()
			def commFin():
				dat = server.req('mark_reservation',self.dat['id'],'complete')
				tkMessageBox.showinfo('Marked Reservation', 'Reservation successfully marked as finished.', parent = root)
				self.root.destroy()
				self.main.reload()
			hotels = server.req('get_all_hotels')
			
			util.window.__init__(self,"SVS HOTELS | View reservation | ID : " + self.dat['id'], width = 600)
			root = self.root

			user_frame = Frame(root, height = 40, width = 580, relief = RAISED, bd = 1)
			user_frame.place(x=10,y=10)

			logout_button = Button(user_frame, text ="back", command=(lambda: root.destroy()))
			logout_button.place(x=330+180, y = 2)

			x,y = 10,6

			label_info = Label(user_frame, text="View reservation ID : "+ self.dat['id'])
			label_info.place(x=x, y = y)

			main_frameH = Frame(root, height = 400, width = 680, relief = RAISED, bd = 0)
			main_frameH.place(x=10,y=60)
			x , y =50, 10

			for i in hotels:
				if i['id'] == self.dat['what'][0]:
					hot = i

			for i in hot[self.dat['what'][1]]:
				if i['id'] == self.dat['what'][2]:
					th = i

			Label(main_frameH, text="Reservation ID : "+ self.dat['id']).place(x=x, y = y)
			Label(main_frameH, text="What :").place(x=x, y = y+30)
			Label(main_frameH, text="Hotel : " + hot['name']).place(x=x+50, y = y+30)
			Label(main_frameH, text="Type : " + self.dat['what'][1]).place(x=x+50, y = y+55)
			Label(main_frameH, text="Type : " + th['name']).place(x=x+50, y = y+80)
			Label(main_frameH, text="Quantity : " + self.dat['quantity']).place(x=x+50, y = y+110)

			Label(main_frameH, text="From : " + "".join([":"+k for k in self.dat['from'][:3]])[1:] + "  " + "".join([":"+k for k in self.dat['from'][3:]])[1:]).place(x=x, y = y+140)
			Label(main_frameH, text="To     : " + "".join([":"+k for k in self.dat['to'][:3]])[1:] + "  " + "".join([":"+k for k in self.dat['to'][3:]])[1:]).place(x=x, y = y+135+30)

			if self.dat['by'][0] == 'a':
				Label(main_frameH, text="By : An administrator with ID : " + self.dat['by'][1]).place(x=x, y = y+160+30)
			else:
				udat = server.req('get_user_details','id',self.dat['by'][1])
				Label(main_frameH, text="By : " + udat[0]['fname'] + " " + udat[0]['lname']).place(x=x, y = y+160+30)
				Label(main_frameH, text=udat[0]['mobile']).place(x=x+30, y = y+185+30)

			Label(main_frameH,text="Status  : ").place(x=x,y=y+210+30)
			if self.dat['confirmed'] == 'False':
				Label(main_frameH,text="To be Confirmed", fg = 'blue').place(x=x+100,y=y+210+30)
			elif self.dat['confirmed'] == 'cancel':
				Label(main_frameH,text="Cancelled", fg = 'red').place(x=x+100,y=y+210+30)
			elif self.dat['confirmed'] == 'complete':
				Label(main_frameH,text="Completed", fg = 'green').place(x=x+100,y=y+210+30)
			else:
				Label(main_frameH,text="Confirmed", fg = 'green').place(x=x+100,y=y+210+30)

			Label(main_frameH, text="Booking time : " + self.dat['booking_time']).place(x=x, y = y+210+60)
			Label(main_frameH, text="Comments : " + self.dat['comments']).place(x=x, y = y+240+60)

			Button(main_frameH,text="Confirm Reservation", command = commCon).place(x=x,y=y+350)
			Button(main_frameH,text="Cancel Reservation", command = commCan).place(x=x+170,y=y+350)
			Button(main_frameH,text="Mark as finished", command = commFin).place(x=x+330,y=y+350)

			root.mainloop()

if __name__ == "__main__":
	server = comm.link('vinay','letmein')
	server.mode = 'a'
	server.login()
	viewRes(server)