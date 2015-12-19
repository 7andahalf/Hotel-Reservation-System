#!/usr/bin/python
from Tkinter import *
import tkMessageBox,Tkinter,comm
import util

class contact(util.window):
	def __init__(self):
		
		# Init
		util.window.__init__(self,"SVS HOTELS | Computerized Reservation System | CONTACT US")

		# Top image
		canvas = Canvas(self.root,width = 600, height = 150, bg = 'white')
		canvas.pack(expand = YES, fill = BOTH)
		gif1 = PhotoImage(file = './data/3.gif')
		canvas.create_image(0, 0, image = gif1, anchor = NW)

		# Frame
		contact_frame = Frame(self.root, height = 265, width = 420, relief = FLAT, bd = 1)
		contact_frame.place(x=90,y=175)

		x,y = 70,20

		# Componenets
		Label(contact_frame, text="S.V.S Hotels computerized reservation system", font=("helvetica", 19)).place(x=x-60, y = y-10)
		Label(contact_frame, text="Contact us", font=("Calibri", 16)).place(x=x+100, y = y+20)
		Label(contact_frame, justify=LEFT, wraplength=350, text = "Reservation Queries:\n\tEmail: reservations@svs.com\n\tTelephone: +91-11-2389 0606\n\tFacsimile : +91-11-2389 0500\n\tAddress: S.V.S Hotels, Bangalore, India").place(x=x-40, y = y+50)
		Label(contact_frame, justify=LEFT, wraplength=350, text = "Customer care:\n\tEmail: custcare@svs.com\n\tTelephone: +91-11-2389 0607\n\tFacsimile : +91-11-2389 0501\n\tAddress: S.V.S Hotels, Bangalore, India").place(x=x-40, y = y+140)
		Button(self.root, text ="back", command=(lambda: self.root.destroy())).place(x=420,y=215)
		
		# run
		self.root.mainloop()

		
if __name__ == "__main__":
	contact()