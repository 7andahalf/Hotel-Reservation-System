#!/usr/bin/python
from Tkinter import *
import tkMessageBox,Tkinter,comm
import util

class forgotPassword(util.window):
	def __init__(self):
		# Verify the given answer
		def verifyans(usern,answer):
			if not comm.link.testConnection():
				tkMessageBox.showerror("Connection Failed", "Connection to the server failed please try again later.")
			else:
				data = comm.link.request("u."+usern+"..forgot_pass_verify." + answer)
				if len(data[0]) > 0 and data[0] != 'Wrong answer':
					tkMessageBox.showinfo("Password", "Your password is: " + data[0])
					self.root.destroy()
				else:
					tkMessageBox.showerror("Wrong answer", "The answer does not match the question.")

		# Check if the username exists, if found change frame to input answer
		def check(usern):
			if not comm.link.testConnection():
				tkMessageBox.showerror("Connection Failed", "Connection to the server failed please try again later.")
			else:
				data = comm.link.request("u."+usern+"..forgot_pass.")
				if len(data[0]) > 0:
					username_frame.destroy()
					# Frame
					answer_frame = Frame(self.root, height = 150, width = 420, relief = RAISED, bd = 1)
					answer_frame.place(x=80,y=175)

					x,y = 70,20

					# Componenets
					label_info = Label(answer_frame, text="Q: " + data[0])
					label_info.place(x=x-35, y = y+0)

					label_answer = Label(answer_frame, text="Answer: ")
					label_answer.place(x=x-35, y = y+30)

					entry_answer = Entry(answer_frame)
					entry_answer.place(x=x+45, y = y+30)

					login_button = Button(answer_frame, text ="Continue", command=(lambda: verifyans(usern,entry_answer.get())))
					login_button.place(x=x+80, y = y+60)

					exit_button = Button(answer_frame, text ="Exit", command=(lambda: self.root.destroy()))
					exit_button.place(x=x+170, y = y+60)
				else:
					tkMessageBox.showerror("Invalid Username", "Username not found.")

		# Init
		util.window.__init__(self,"SVS HOTELS | Computerized Reservation System | FORGOT PASSWORD",height=350)

		# Top image
		canvas = Canvas(width = 600, height = 150, bg = 'white')
		canvas.pack(expand = YES, fill = BOTH)
		gif1 = PhotoImage(file = './data/3.gif')
		canvas.create_image(0, 0, image = gif1, anchor = NW)


		# Frame
		username_frame = Frame(self.root, height = 150, width = 420, relief = RAISED, bd = 1)
		username_frame.place(x=80,y=175)

		x,y = 70,20

		# Componenets
		label_info = Label(username_frame, text="Forgot password? Please enter username to continue")
		label_info.place(x=x-35, y = y+0)

		label_usern = Label(username_frame, text="Username: ")
		label_usern.place(x=x+0, y = y+30)

		entry_usern = Entry(username_frame)
		entry_usern.place(x=x+80, y = y+30)

		login_button = Button(username_frame, text ="Continue", command=(lambda: check(entry_usern.get())))
		login_button.place(x=x+80, y = y+60)

		exit_button = Button(username_frame, text ="Back", command=(lambda: self.root.destroy()))
		exit_button.place(x=x+170, y = y+60)
	
		# run
		self.root.mainloop()

if __name__ == "__main__":
	forgotPassword()