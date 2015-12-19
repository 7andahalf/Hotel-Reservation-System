#!/usr/bin/python
from Tkinter import *
import tkMessageBox,Tkinter,comm
import util

class register(util.window):
	def __init__(self):
		# Check the entries for proper entries and pass on the request to the server
		def check():
			if not comm.link.testConnection():
				tkMessageBox.showerror("Connection Failed", "Connection to the server failed please try again later.")
			else:
				data = [entry_usern.get(),entry_passw.get(), entry_fname.get(), entry_lname.get(),gender.get(), entry_mobile.get(),  secque.get(), entry_secans.get()]
				aok = True
				for i in data:
					if len(i) == 0 and aok:
						tkMessageBox.showerror("Invalid Entry", "Please fill in all the details")
						aok = False
				if entry_passw.get() != entry_cpassw.get() and aok:
					tkMessageBox.showerror("Invalid Entry", "Passwords must match")
					aok = False
				if aok:
					message = ("".join([","+str(i) for i in data]))[1:]
					data = comm.link.request("...register_user."+message)
					if data[0] == 'successful registration':
						tkMessageBox.showinfo("Registration Successful", "You have successfully registered")
						self.root.destroy()
					else:
						tkMessageBox.showerror("Registration Failed", "The username might be already taken. Do not used full stops or any other charectors in entries ")


		# create window and its widgets
		util.window.__init__(self,"SVS HOTELS | Computerized Reservation System | REGISTRATION")

		canvas = Canvas(width = 600, height = 150, bg = 'white')
		canvas.pack(expand = YES, fill = BOTH)
		gif1 = PhotoImage(file = './data/3.gif')
		canvas.create_image(0, 0, image = gif1, anchor = NW)

		register_frame = Frame(self.root, height = 330, width = 580, relief = RAISED, bd = 1)
		register_frame.place(x=10,y=160)

		x= 10
		y= 50

		label_info = Label(register_frame, text="Please enter your details to register")
		label_info.place(x=x+40, y = y-20)

		label_user = Label(register_frame, text="First name: ")
		label_user.place(x=x+0, y = y+30)
		entry_fname = Entry(register_frame)
		entry_fname.place(x=x+80, y = y+30)

		label_lname = Label(register_frame, text="Last name: ")
		label_lname.place(x=x+280, y = y+30)
		entry_lname = Entry(register_frame)
		entry_lname.place(x=x+360, y = y+30)

		label_usern = Label(register_frame, text="Username: ")
		label_usern.place(x=x+0, y = y+60)
		entry_usern = Entry(register_frame)
		entry_usern.place(x=x+80, y = y+60)

		label_passw = Label(register_frame, text="Password: ")
		label_passw.place(x=x+0, y = y+90)
		entry_passw = Entry(register_frame, show = "*")
		entry_passw.place(x=x+80, y = y+90)

		label_cpassw = Label(register_frame, text="Confirm: ")
		label_cpassw.place(x=x+280, y = y+90)
		entry_cpassw = Entry(register_frame, show = "*")
		entry_cpassw.place(x=x+360, y = y+90)

		label_mobile = Label(register_frame, text="Mobile No: ")
		label_mobile.place(x=x+0, y = y+120)
		entry_mobile = Entry(register_frame)
		entry_mobile.place(x=x+80, y = y+120)

		gender = StringVar(register_frame)
		gender.set("")
		label_gender = Label(register_frame, text="Gender: ")
		label_gender.place(x=x+280, y = y+120)
		pick_gender = OptionMenu(register_frame,gender, "male", "female", "other")
		pick_gender.place(x=x+360, y = y+120)

		secque = StringVar(register_frame)
		secque.set("")
 		label_secque = Label(register_frame, text="Security Question: ")
		label_secque.place(x=x, y = y+150)
		pick_secque = OptionMenu(register_frame,secque, "Where was your father born", "What was your first pets name", "What is the name of your best friend", "Which is your favorite colour", "Which was your first school")
		pick_secque.place(x=x+140, y = y+150)

		label_secans = Label(register_frame, text="Answer :")
		label_secans.place(x=x+0, y = y+180)
		entry_secans = Entry(register_frame)
		entry_secans.place(x=x+80, y = y+180)

		register_button = Button(register_frame, text ="Register", command=(lambda: check()))
		register_button.place(x=x+80, y = y+210)

		exit_button = Button(register_frame, text ="Back", command=(lambda: self.root.destroy()))
		exit_button.place(x=x+480, y = y-25)

		self.root.mainloop()


if __name__ == "__main__":
	register()