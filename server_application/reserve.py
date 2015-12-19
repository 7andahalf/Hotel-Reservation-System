
from db import database
import hotel

'''
Structure of reservations database

id  : by  : what : from    : to       : booking_time : confirmed : ended : comments : total_amount : quantity : reason : other
str   lst   lst    6-tuple   6-tuple    6-tuple        str         str     str        str            str        str      str

by : ['a', '0'] or ['u', '1'] etc.

what : ['0', 'rooms', '0'] etc.
       [hotel_id, type, thing_id]
    types :
       'rooms' : rooms
       'banquet' : banquet
       'meeting' : meeting
       'restaurants' : restaurants

from, to, booking_time : (12,12,2015,12,45,00) etc.
                         (DD,MM,YYYY,HH,MM,SS)
'''

# Adds a reservation to the database. needs data as a dictionary. ID will be automatically generated
def addReservation(data):
    if possibleReservation(data['what'],data['from'],data['to']) <= 0:
        return False
    if possibleReservation(data['what'],data['from'],data['to']) - int(data['quantity']) < 0:
        return False
    reservations = database("reservations")
    util = database("util")
    data['id'] = str(util.get("name","num_reservations")[0]['value'])
    if reservations.insert(data):
    	util.change("name","num_reservations","value",util.get("name","num_reservations")[0]['value']+1)
    	return True
    else:
    	return False

# Get all bookings of a particular place
def getBookings(what):
    return database("reservations").get("what",what)

# Check if something is available at the given time and return total availabilities
def possibleReservation(what, fro, to):
    def greaterDate(one,two):
        if int(one[2]) > int(two[2]):return True
        elif int(one[2]) < int(two[2]): return False
        if int(one[1]) > int(two[1]):return True
        elif int(one[1]) < int(two[1]): return False
        if int(one[0]) > int(two[0]):return True
        elif int(one[0]) < int(two[0]): return False
        if int(one[3]) > int(two[3]):return True
        elif int(one[3]) < int(two[3]): return False
        if int(one[4]) > int(two[4]):return True
        elif int(one[4]) < int(two[4]): return False
        if int(one[5]) >= int(two[5]):return True
        elif int(one[5]) < int(two[5]): return False
    totalWhats = [i['quantity'] for i in hotel.getHotel("id",what[0])[0][what[1]] if i['id'] == what[2]][0]
    for i in getBookings(what):
        if i['confirmed'] != 'cancel':
            if not (greaterDate(i['from'],to) or greaterDate(fro,i['to'])):
                totalWhats -= int(i['quantity'])
    return totalWhats

# Changes a particular reservation
def changeReservation(id, value):
    return database("reservations").change('id',id,'confirmed',value)

# Gets a particular reservation
def getReservation(name, value):
    return database("reservations").get(name,value)

# Gets all reservations
def getAllReservations():
    return database("reservations").rows

# Testcases    
'''
if __name__ == "__main__":
    print addReservation({
            'by' : ['a', '0'],
            'what' : ['0', 'rooms', '0'],
            'from' : (17,11,2015,0,0,0),
            'to' : (18,11,2015,0,0,0),
            'booking_time' : (1,11,2015,12,34,43),
            'confirmed' : 'True',
            'ended' : 'False',
            'comments' : "",
            'total_amount' : 10203,
            'quantity' : 2,
            'reason' : "Y U WANT?",
            'other' : "nope"
        })
    print possibleReservation(['0', 'rooms', '0'],(11,11,2015,0,0,0),(19,11,2015,0,0,0))
'''


