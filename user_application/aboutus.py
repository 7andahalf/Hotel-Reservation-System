#!/usr/bin/python
from Tkinter import *
import tkMessageBox,Tkinter,comm
import util

class about(util.window):
	def __init__(self):
		
		# Init
		util.window.__init__(self,"SVS HOTELS | Computerized Reservation System | ABOUT")

		# Top image
		canvas = Canvas(self.root,width = 600, height = 150, bg = 'white')
		canvas.pack(expand = YES, fill = BOTH)
		gif1 = PhotoImage(file = './data/3.gif')
		canvas.create_image(0, 0, image = gif1, anchor = NW)

		# Frame
		aboutFrame = Frame(self.root, height = 265, width = 420, relief = FLAT, bd = 1)
		aboutFrame.place(x=90,y=175)

		x,y = 70,20

		# Componenets
		Label(aboutFrame, text="S.V.S Hotels computerized reservation system", font=("helvetica", 19)).place(x=x-60, y = y-10)
		Label(aboutFrame, text="v1.0", font=("Calibri", 16)).place(x=x+120, y = y+20)
		Label(aboutFrame, justify=CENTER, wraplength=350, text = "Founded in 1451, S.V.S International Hotels represents a collection of distinct, upscale hotels and resorts known for its central locations and quality throughout the world with over hundreds of hotels worldwide. An elegant and welcoming ambience makes it easy for guests to focus on work as well as play. Discover our unique tales steeped in deep-rooted origins and celebrate local traditions as we bring our heritage to life.").place(x=x-40, y = y+50)
		Button(self.root, text ="back", command=(lambda: self.root.destroy())).place(x=270,y=400)
		
		# run
		self.root.mainloop()

		
if __name__ == "__main__":
	about()