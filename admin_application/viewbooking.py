#!/usr/bin/python
from Tkinter import *
import tkMessageBox,Tkinter,comm
import util

class viewbookings(util.window):
	def __init__(self, server):
			util.window.__init__(self,"SVS HOTELS | View bookings")
			root = self.root

			user_frame = Frame(root, height = 40, width = 580, relief = RAISED, bd = 1)
			user_frame.place(x=10,y=10)

			logout_button = Button(user_frame, text ="back", command=(lambda: root.destroy()))
			logout_button.place(x=330+180, y = 2)

			x,y = 10,6

			label_info = Label(user_frame, text="View all the previous bookings: ")
			label_info.place(x=x, y = y)

			main_frameH = Frame(root, height = 400, width = 580, relief = RAISED, bd = 0)
			main_frameH.place(x=10,y=60)

			data = server.req('get_user_bookings')

			def components():
				j = 0
				for i in data:
					subFrame = Frame(Hframe, height=140, width = 550, relief = RAISED, bd = 1)
					subFrame.grid(row=j,column=0)
					hotel = server.req('get_hotel_by_id',i['what'][0])[0]
					thing = None
					for k in hotel[i['what'][1]]:
						if k['id'] == i['what'][2]:
							thing = k

					Label(subFrame,text=str(j+1)+". " + i['what'][1] + " : " + thing['name']).place(x=5,y=7)
					Label(subFrame,text="ID: " + i['id']).place(x=500,y=7)
					Label(subFrame,text="Hotel: "+hotel['name']).place(x=40,y=30)
					Label(subFrame,text="From: "+i['from'][0]+"/"+i['from'][1]+"/"+i['from'][2]).place(x=40,y=55)
					Label(subFrame,text="To  : "+i['to'][0]+"/"+i['to'][1]+"/"+i['to'][2]).place(x=240,y=55)
					Label(subFrame,text="Quantity  : "+i['quantity']).place(x=40,y=80)
					Label(subFrame,text="Status  : ").place(x=240,y=80)
					if i['confirmed'] == 'False':
						Label(subFrame,text="To be Confirmed", fg = 'blue').place(x=310,y=80)
					elif i['confirmed'] == 'cancel':
						Label(subFrame,text="Cancelled", fg = 'red').place(x=310,y=80)
					elif i['confirmed'] == 'complete':
						Label(subFrame,text="Completed", fg = 'green').place(x=310,y=80)
					else:
						Label(subFrame,text="Confirmed", fg = 'green').place(x=310,y=80)
					Label(subFrame,text="Booking time  : "+i['booking_time']).place(x=40,y=105)
					j+=1

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

if __name__ == "__main__":
	server = comm.link('aravind','iamaravind')
	server.login()
	viewbookings(server)
