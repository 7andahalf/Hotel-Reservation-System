#!/usr/bin/python
from Tkinter import *
import tkMessageBox,Tkinter,comm
import util

class viewHotels(util.window):
	def __init__(self, server):
		if not server.testConnection():
			tkMessageBox.showerror("Connection Failed", "Connection to the server failed please try again later.")
			self.root.destroy()
		udata = server.req('get_user_details')
		hotels = server.req('get_all_hotels')

		util.window.__init__(self,"SVS HOTELS | Computerized Reservation System | All hotels")

		canvas = Canvas(width = 600, height = 150, bg = 'white')
		canvas.pack(expand = YES, fill = BOTH)
		gif1 = PhotoImage(file = './data/3.gif')
		canvas.create_image(0, 0, image = gif1, anchor = NW)

		user_frame = Frame(self.root, height = 40, width = 580, relief = RAISED, bd = 1)
		user_frame.place(x=10,y=165)

		logout_button = Button(user_frame, text ="back", command=(lambda: self.root.destroy()))
		logout_button.place(x=330+180, y = 2)

		x,y = 10,6

		label_info = Label(user_frame, text="All hotels")
		label_info.place(x=x, y = y)

		main_frame = Frame(self.root, height = 260, width = 580, relief = RAISED, bd = 0)
		main_frame.place(x=10,y=215)

		def data():
			j = 0
			for i in hotels:
				subFrame = Frame(frame, height = 40, width = 550, relief = RAISED, bd = 1)
				subFrame.grid(row=j,column=0)
				Label(subFrame,text=str(j+1)+".").place(x=5,y=7)
				Label(subFrame,text=i['name']).place(x=30,y=7)
				Button(subFrame, text ="View", command=view(i).show).place(x=470,y=4)
				j+=1

		def myfunction(event):
		    canvas.configure(scrollregion=canvas.bbox("all"),width=557,height=260)

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

class view(util.window):
	def __init__(self,d):
		self.data = d
	def show(self):
			dat = self.data

			util.window.__init__(self,"SVS HOTELS | " + dat['name'])

			root = self.root

			user_frame = Frame(root, height = 40, width = 580, relief = RAISED, bd = 1)
			user_frame.place(x=10,y=10)

			logout_button = Button(user_frame, text ="back", command=(lambda: root.destroy()))
			logout_button.place(x=330+180, y = 2)

			x,y = 10,6

			label_info = Label(user_frame, text="View hotel: "  + dat['name'])
			label_info.place(x=x, y = y)

			main_frameH = Frame(root, height = 400, width = 580, relief = RAISED, bd = 0)
			main_frameH.place(x=10,y=60)

			def components():
				j = 0

				Label(Hframe,text=dat['description'],wraplength=540,justify=LEFT).grid(row=j,column=0)
				j+=1

				if len(dat['rooms']) > 0:
					subFrame = Frame(Hframe, height=40, width = 550, relief = RAISED, bd = 0)
					subFrame.grid(row=j,column=0)
					Label(subFrame,text='Rooms available for booking:', font=("helvetica", 19)).place(x=5,y=7)
					j+=1

				for i in dat['rooms']:
					Label(Hframe,text=i['name'],wraplength=540,justify=LEFT, font=("helvetica", 15)).grid(row=j,column=0)
					Label(Hframe,text="\t"+i['description'],wraplength=540,justify=LEFT).grid(row=j+1,column=0)
					j+=2

				if len(dat['banquet']) > 0:
					subFrame = Frame(Hframe, height=40, width = 550, relief = RAISED, bd = 0)
					subFrame.grid(row=j,column=0)
					Label(subFrame,text='Banquet halls available for booking:', font=("helvetica", 19)).place(x=5,y=7)
					j+=1

				for i in dat['banquet']:
					Label(Hframe,text=i['name'],wraplength=540,justify=LEFT, font=("helvetica", 15)).grid(row=j,column=0)
					Label(Hframe,text="\t"+i['description'],wraplength=540,justify=LEFT).grid(row=j+1,column=0)
					j+=2

				if len(dat['meeting']) > 0:
					subFrame = Frame(Hframe, height=40, width = 550, relief = RAISED, bd = 0)
					subFrame.grid(row=j,column=0)
					Label(subFrame,text='Meeting rooms available for booking:', font=("helvetica", 19)).place(x=5,y=7)
					j+=1

				for i in dat['meeting']:
					Label(Hframe,text=i['name'],wraplength=540,justify=LEFT, font=("helvetica", 15)).grid(row=j,column=0)
					Label(Hframe,text="\t"+i['description'],wraplength=540,justify=LEFT).grid(row=j+1,column=0)
					j+=2

				if len(dat['restaurants']) > 0:
					subFrame = Frame(Hframe, height=40, width = 550, relief = RAISED, bd = 0)
					subFrame.grid(row=j,column=0)
					Label(subFrame,text='Restaurants available for booking:', font=("helvetica", 19)).place(x=5,y=7)
					j+=1

				for i in dat['restaurants']:
					Label(Hframe,text=i['name'],wraplength=540,justify=LEFT, font=("helvetica", 15)).grid(row=j,column=0)
					Label(Hframe,text="\t"+i['description'],wraplength=540,justify=LEFT).grid(row=j+1,column=0)
					j+=2

				subFrame = Frame(Hframe, height=40, width = 550, relief = RAISED, bd = 0)
				subFrame.grid(row=j,column=0)
				Label(subFrame,text='Location:', font=("helvetica", 19)).place(x=5,y=7)
				j+=1

				Label(Hframe,text=dat['address'],wraplength=540,justify=LEFT).grid(row=j,column=0)
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
	server = comm.link('vinay','letmein')
	server.login()
	viewHotels(server)