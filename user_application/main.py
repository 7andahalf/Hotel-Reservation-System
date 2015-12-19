#!/usr/bin/python


# Loading window opens
# Exits if connection to server fails
import loading
load = loading.loading()
if load.status['loading'] == 'fail':
	exit()
goto = 'login'

# Loop so that one window can refer several other windows
while goto != None:
	nextGoto = None
	# Login window
	if goto == 'login':
		import login
		log = login.login()
		if log.status['login'] == 'forgotpass':
			import forgotpass
			forgotpass.forgotPassword()
			nextGoto = 'login'
		elif log.status['login'] == 'register':
			import register
			register.register()
			nextGoto = 'login'
		elif log.status['login'] == 'pass':
			server = log.server
			nextGoto = 'home'
		else:
			exit()

	# Home window
	if goto == 'home':
		import home
		hom = home.home(server)
		nextGoto = 'login'
		if hom.status['home'] == 'viewhotels':
			import viewhotels
			viewhotels.viewHotels(server)
			nextGoto = 'home'
		if hom.status['home'] == 'reserve':
			import reserve
			reserve.book(server,hom.reser)
			nextGoto = 'home'
		if hom.status['home'] == 'viewbooking':
			import viewbooking
			viewbooking.viewbookings(server)
			nextGoto = 'home'
		if hom.status['home'] == 'aboutus':
			import aboutus
			aboutus.about()
			nextGoto = 'home'
		if hom.status['home'] == 'contactus':
			import contactus
			contactus.contact()
			nextGoto = 'home'
	goto = nextGoto