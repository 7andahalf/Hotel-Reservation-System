

import hotel,admins,users,reserve,datetime

'''
This is the router script. It takes in incoming queries processes them
and returns the result to the server.
'''

def query(data):
	try:
		asker, usern, passw, task, param = data.split(".")
		params = param.split(",")
		if asker == 'u' and users.authUser(usern,passw): pass
		elif asker == 'a' and admins.authAdmin(usern,passw): pass
		elif task != 'register_user' and task != 'forgot_pass_verify' and task != 'forgot_pass': return ['error', 'Authentication invalid']
	except:
		return ['error', 'improper API format']

	# P : 1
	if task == 'get_user_details':
		if asker == 'u':
			return users.secureData(users.getUser('username',usern)[0])
		elif asker == 'a':
			if 1 in admins.getPerm(usern):
				if len(params[0]) == 0:
					return admins.secureData(admins.getAdmin('username',usern)[0])
				try:
					return [users.secureData(i) for i in users.getUser(params[0],params[1])]
				except:
					return ['error', 'parameters invalid']
			else:
				return ['error', 'Permission denied']

	# P : None
	if task == 'get_all_hotels':
		return [hotel.secureData(i) for i in hotel.getAllHotels()]

	# P : None
	if task == 'get_hotel_by_id':
		return [hotel.secureData(i) for i in hotel.getHotel('id',params[0])]

	# P : None
	if task == 'forgot_pass' and asker == 'u':
		return [users.secQue(usern)]

	# P : None
	if task == 'forgot_pass_verify' and asker == 'u':
		return [users.verSecAns(usern, params[0])]

	# P : None
	if task == 'register_user':
		data = {}
		if len(params) < 8:
			return ['registration failed']
		data['username'] = params[0]
		data['password'] = params[1]
		data['fname'] = params[2]
		data['lname'] = params[3]
		data['gender'] = params[4]
		data['mobile'] = params[5]
		data['secque'] = params[6]
		data['secans'] = params[7]
		if users.addUser(data):
			return ['successful registration']
		else:
			return ['registration failed']

	# P : None
	if task == 'availability':
		if len(params) < 15:
			return ['error', 'parameters invalid']
		return [reserve.possibleReservation(params[0:3],params[3:9],params[9:15])]

	# P : None
	if task == 'make_reservation':
		data = {}
		if len(params) < 20:
			return ['reservation failed']
		if asker == 'u':
			data['by'] = ['u', users.getUser('username',usern)[0]['id']]
		else:
			data['by'] = ['a', admins.getAdmin('username',usern)[0]['id']]
		data['what'] = params[0:3]
		data['from'] = params[3:9]
		data['to'] = params[9:15]
		data['booking_time'] = datetime.datetime.now()
		data['confirmed'] = 'False'
		data['ended'] = 'False'
		data['comments'] = params[15]
		data['total_amount'] = params[16]
		data['quantity'] = params[17]
		data['reason'] = params[18]
		data['other'] = params[19]
		if reserve.addReservation(data):
			return ['successful reservation']
		else:
			return ['reservation failed']

	# P : 2
	if task == 'get_user_bookings':
		if asker == 'u':
			return reserve.getReservation("by", ['u', users.getUser('username',usern)[0]['id']])
		elif asker == 'a':
			if 2 in admins.getPerm(usern):
				if len(params[0]) == 0:
					return reserve.getReservation("by", ['a', admins.getAdmin('username',usern)[0]['id']])
				try:
					return reserve.getReservation("by", ['u', users.getUser(params[0],params[1])[0]['id']])
				except:
					return ['error', 'parameters invalid']
			else:
				return ['error', 'Permission denied']

	# P : None
	if task == 'get_allbookings_of' and asker == 'a':
		data = reserve.getAllReservations()
		if len(params[0]) == 0:
			return data
		elif len(params) == 1:
			return [i for i in data if i['what'][0] == params[0]]
		elif len(params) == 2:
			return [i for i in data if (i['what'][0] == params[0]) and (i['what'][1] == params[1])]
		elif len(params) == 3:
			return [i for i in data if (i['what'][0] == params[0]) and (i['what'][1] == params[1]) and (i['what'][2] == params[2])]
		return ['error', 'parameters invalid']

	# P : None
	if task == 'mark_reservation' and asker == 'a':
		if len(params) < 2:
			return ['error', 'parameters invalid']
		data = reserve.changeReservation(params[0],params[1])
		return [data]

	# P : None
	if task == 'get_all_users' and asker == 'a':
		data = [users.secureData(i) for i in users.getAllUsers()]
		return data

	return ['successful login']

# Test cases
'''
if __name__ == "__main__":
    print addHotel({'users':[1,2],'banquet':[],'rooms':[["hola"],["hola2"]],'address':["bang"],'restaurants':[123],'meeting':[],'name':"the seven seas"})
    print getAllHotels()
    print query('a.vinay.123.d.e')
    print query("a.vinay.letmein.get_user_details.")
    print query('u.ruby.bowbow.availability.0,restaurants,0,11,12,2015,0,0,0,12,12,2015,0,0,0')
    print query('u.ruby.bowbow.make_reservation.0,restaurants,0,11,12,2015,0,0,0,12,12,2015,0,0,0,,100,99,none,')
    print query('u.ruby.bowbow.availability.0,restaurants,0,11,12,2015,0,0,0,12,12,2015,0,0,0')
    print query('a.admin.letmein.get_user_bookings.fname,Ruby')
    print query('a.admin.letmein.get_allbookings_of.0,restaurants,0')
    print query('u...forgot_pass.vinay')
'''


