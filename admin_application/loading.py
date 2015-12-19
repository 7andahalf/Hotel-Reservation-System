#!/usr/bin/python
from Tkinter import *
import tkMessageBox,Tkinter,comm
import util

class loading(util.window):
	def __init__(self):
		# Init
		util.window.__init__(self,"",tb=False,height=300)	

		# image
		canvas = Canvas(width = 600, height = 300, bg = 'white')
		canvas.pack(expand = YES, fill = BOTH)
		gif1 = PhotoImage(file = './data/1.gif')
		canvas.create_image(0, 0, image = gif1, anchor = NW)

		# run this after 3 secs
		self.root.after(3000, self.check)
		self.status['loading'] = 'active'

		# run
		self.root.mainloop()

	# check connection to server. Exit if fails
	def check(self):
		if comm.link.testConnection():
			self.status['loading'] = 'pass'
			self.root.destroy()
		else:
			self.status['loading'] = 'fail'
			tkMessageBox.showerror("Connection Failed", "Connection to the server failed please try again later.")
			self.root.destroy()

if __name__ == "__main__":
	loading()