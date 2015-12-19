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

		x,y = 10,6
		
		logout_button = Button(user_frame, text ="back", command=(lambda: self.root.destroy()))
		logout_button.place(x=330+180, y = 2)

		label_info = Label(user_frame, text="View Reservations")
		label_info.place(x=x, y = y)

		main_frame = Frame(self.root, height = 260, width = 580, relief = RAISED, bd = 0)
		main_frame.place(x=10,y=215)

		x,y = 110,6

		label_info = Label(main_frame, text="Fill only the options that you want to be considered")
		label_info.place(x=x, y = y+10)

		Label(main_frame, text="What(ID):").place(x=x+20, y = y+40)
		entry_what = Entry(main_frame)
		entry_what.place(x=x+120, y = y+40)

		Label(main_frame, text="Who(ID):").place(x=x+20, y = y+70)
		entry_who = Entry(main_frame)
		entry_who.place(x=x+120, y = y+70)

		Label(main_frame, text="After:").place(x=x+20, y = y+100)
		entry_aft = Entry(main_frame)
		entry_aft.place(x=x+120, y = y+100)

		Label(main_frame, text="Before:").place(x=x+20, y = y+130)
		entry_bef = Entry(main_frame)
		entry_bef.place(x=x+120, y = y+130)

		Label(main_frame, text="Res ID:").place(x=x+20, y = y+160)
		entry_rid = Entry(main_frame)
		entry_rid.place(x=x+120, y = y+160)

		Label(main_frame, text="Status:").place(x=x+20, y = y+190)
		stat = StringVar(main_frame)
		stat.set("") 
		OptionMenu(main_frame, stat, "False", "cancel", "complete", "confirm").place(x = x + 120, y= y+ 190)

		view_button = Button(main_frame, text ="View Reservations", command=(lambda: view(entry_what.get(), entry_who.get(), entry_aft.get(), entry_bef.get(), stat.get(),entry_rid.get(), server)))
		view_button.place(x=x+90, y = 230)

		self.root.mainloop()

# Views the reservations that are in the given criteria
class view(util.window):
	def __init__(self,what,who,aft,bef,stat,rid,server):
			self.what = what
			self.who = who
			self.aft = aft
			self.bef = bef
			self.stat = stat
			self.rid = str(rid)
			self.server = server

			try:
				aft = [int(i) for i in self.aft.split(":")]
				if len(aft) != 6:
					raise Exception
			except:
				aft = ""

			try:
				bef = [int(i) for i in self.bef.split(":")]
				if len(bef) != 6:
					raise Exception
			except:
				bef = ""

			try:
				what = [str(i) for i in self.what.split(":")]
			except:
				what = ""

			try:
				who = [str(i) for i in self.who.split(":")]
			except:
				who = ""


			self.what = what
			self.who = who
			self.aft = aft
			self.bef = bef
			self.stat = stat

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
			root = self.root
			server = self.server
			hotels = server.req('get_all_hotels')
			main_frameH = Frame(root, height = 400, width = 680, relief = RAISED, bd = 0)
			main_frameH.place(x=10,y=60)
			self.mainfr = main_frameH

			data = server.req('get_allbookings_of')
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
					try:
						if len(self.what[0]) != 0:
							if len(self.what) >= 1:
								if not i['what'][0] == self.what[0]:
									raise Exception
							if len(self.what) >= 2:
								if not i['what'][1] == self.what[1]:
									raise Exception
							if len(self.what) == 3:
								if not i['what'][2] == self.what[2]:
									raise Exception

						if len(self.who[0]) != 0:
							if len(self.who) >= 1:
								if not i['by'][0] == self.who[0]:
									raise Exception
							if len(self.who) >= 2:
								if not i['by'][1] == self.who[1]:
									raise Exception

						if self.stat != "":
							if not i['confirmed'] == self.stat:
								raise Exception

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
							if int(one[5]) >= int(two[5]):return True
							elif int(one[5]) < int(two[5]): return False

						if self.aft != "":
							if not greaterDate(i['from'],self.aft):
								raise Exception

						if self.bef != "":
							if greaterDate(i['to'],self.bef):
								raise Exception

						if self.rid != "":
							if i['id'] != self.rid:
								raise Exception

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
					except:
						pass


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