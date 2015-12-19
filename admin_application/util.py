#!/usr/bin/python
from Tkinter import *
import tkMessageBox,Tkinter,comm

class window:
	# useful 
	status = {}

	# centers screen
	def center(self,root,w,h):
		ws = root.winfo_screenwidth()
		hs = root.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		root.geometry('%dx%d+%d+%d' % (w, h, x, y))

	def __init__(self,title,tb = True, height = 500, width = 600):
		self.root = Tkinter.Tk()
		if not tb:
			self.root.overrideredirect(1)
		#self.root.iconbitmap('./data/hms.ico')
		self.root.resizable(width=FALSE, height=FALSE)
		self.root.title(title)
		self.center(self.root,width,height)
