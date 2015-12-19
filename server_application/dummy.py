
import hotel,admins,users,db

'''
This script creates dummy data in the server
'''

util = db.database("util")
admin = db.database("admins")
user = db.database("users")
hotels = db.database("hotels")
reservations = db.database("reservations")

# write utils

util.addColumn("name")
util.addColumn("value")
util.insert({
		'name' : 'num_users',
		'value' : 0
	})
util.insert({
		'name' : 'num_admins',
		'value' : 0
	})
util.insert({
		'name' : 'num_hotels',
		'value' : 0
	})
util.insert({
		'name' : 'num_reservations',
		'value' : 0
	})

print "Utils: done"
print db.database("util").data
print ""


# add two admins
admin.addColumn("id")
admin.addColumn("username")
admin.addColumn("password")
admin.addColumn("name")
admin.addColumn("permissions")

admins.addAdmin({
		'username' : 'admin',
		'password' : 'letmein',
		'name' : 'Mr Howard Wolawitz',
		'permissions' : [1,2,3,4,5]
	})

admins.addAdmin({
		'username' : 'vinay',
		'password' : 'letmein',
		'name' : 'Mr Vinay C K',
		'permissions' : [1,2,3,4,5]
	})

print "Admin: done"
print db.database("admins").data
print ""

# add 2 users

user.addColumn("id")
user.addColumn("username")
user.addColumn("password")
user.addColumn("fname")
user.addColumn("lname")
user.addColumn("gender")
user.addColumn("mobile")
user.addColumn("secque")
user.addColumn("secans")

users.addUser({
		'username' : 'vinay',
		'password' : 'letmein',
		'fname' : 'Vinay',
		'lname' : 'C K',
		'gender' : 'male',
		'mobile' : '8277104526',
		'secque' : 'What is your dogs name?',
		'secans' : 'ruby'
	})

users.addUser({
		'username' : 'adarsh',
		'password' : 'letmein',
		'fname' : 'Adarsh',
		'lname' : 'Katagihallimath',
		'gender' : 'male',
		'mobile' : '9447756566',
		'secque' : 'What is you brothers name?',
		'secans' : 'vinay'
	})

print "Users: done"
print db.database("users").data
print ""

# add hotel
hotels.addColumn("id")
hotels.addColumn("users")
hotels.addColumn("name")
hotels.addColumn("address")
hotels.addColumn("rooms")
hotels.addColumn("banquet")
hotels.addColumn("meeting")
hotels.addColumn("restaurants")
hotels.addColumn("description")

hotel.addHotel({
		'users' : ['0', '1'],
		'name' : "Hotel Princess Montenegro",
		'description': "HOTEL PRINCESS (4 stars) is located at the most attractive part of Bar, nearby the promenade along the sea shore, and is surrounded by lush vegetation, museum complex and sport terraines. Rooms and apartments are comfortable and contemporarily designed, with exceptional views of the marina, beach and sea, palace and mountains at the town s hinterland. Hotel has 135 rooms, which offer modern comfort: mini bar, air conditioner, satelite & cable TV, safety deposit box, as well as all neccessary accesories and room service. Choose the bathroom you want: with bath tub and shower bath tub; only with bath tub or only with shower bath tub. Our restaurants offer specialties of national & international cuisine, various drinks, accompanied with good service. Lobby & Piano bar are pleasant spaces for rest, while having a drink and conversation with business partners or friends. You can enjoy and also have a drink or try some sweets or cakes at the Pool bar, from which you can go out to the pool and spacious terrace of the hotel.",
		'address' : "Jovana Tomasevica 21\n85000 Bar, Montenegro\nTel: +382 30 300 100 ; +382 30 300 300\nFax: +382 30 312 510\nEmail: reservations@hotelprincess.svs.com",
		'rooms' : [{
		        'id' : '0',
		        'name' : "STANDARD DOUBLE ROOM",
		        'price' : 10400,
		        'description' : 'Standard double room (25m2), out of which there are 72 connected rooms where it is possible to connect, which is ideal for accommodation of parents and children.9 direct sea view 42 side sea view 55 park view',
		        'quantity' : 72
		    },
		    {
		        'id' : '1',
		        'name' : "DELUXE SUITE APARTMANA",
		        'price' : 33500,
		        'description' : 'Deluxe suite is a three-room, comfortable apartment which is consisted of living room, two bedrooms and two bathrooms. The apartments have direct sea view and park view. Maximal number of persons: four adults and two children.',
		        'quantity' : 4
		    },
		    {
		        'id' : '2',
		        'name' : "JUNIOR SUITE APARTMENT",
		        'price' : 13500,
		        'description' : 'Junior suites are consisted of living room and bedroom. The apartments have sea and park view.',
		        'quantity' : 10
		    },
		    {
		        'id' : '3',
		        'name' : "DISABLE",
		        'price' : 3500,
		        'description' : 'Specially equipped rooms in order to satisfy the needs of people with limited physical capabilities. Park view.',
		        'quantity' : 2
		    }],
		'banquet' : [{
		        'id' : '0',
		        'name' : "The main hall",
		        'price' : 20000,
		        'description' : 'the area 150m2, has 120 seats (classroom), 150 seats (Theatat) and 50 seats (form II) and two smaller rooms, land 70m2, have the following capacity: 40 seats (Classroom), 50 seats (Theatat) and 25 seats (form II). In each room is modern audio-visual equipment PC and printer, projector, screen (Dimension 240 x 240), DVD, TV, video, flip chart, speakers and Internet access. There is the possibility of using fax, copier and printer equipment. In the immediate vicinity of these spaces is the lobby bar, an ideal place for a coffee break, and the Banketsaal, a place where their business lunch in a Erhohlung for all your senses transforms! Capacity: 80 seats',
		        'seating' : 150,
		        'quantity' : 3
		    }],
		'meeting' : [{
		        'id' : '0',
		        'name' : "The seven seas",
		        'price' : 10000,
		        'description' : 'The Benedict Room is a multi-purpose room. The room is equipped with four rectangular tables, allowing multiple room configurations. Tables may be removed for discussion and prayer circles. The room is AV equipped with PC-compatible projection equipment. Dry erase board and easels are available.',
		        'seating' : 30,
		        'quantity' : 1
		    }],
		'restaurants' : [{
		        'id' : '0',
		        'name' : "The Northern Scarf",
		        'description' : 'All day dining, multi-cuisine, bistro style restaurant, offers the best of world cuisine.',
		        'quantity' : 100
		    }]
	})

hotel.addHotel({
		'users' : ['0', '1'],
		'name' : "The Regaalis",
		'description': "The Regaalis is a boutique hotel that is located in the heart of Bangalore, offers all modern amenities in a contemporary classical ambiance. This Bangalore hotel contains luxury facilities in unique or intimate settings with full service accommodations.",
		'address' : "36/C Hosur road\nElectronic city\nMangalore - 567201\nTel: +382 30 300 100 ; +382 30 300 300\nFax: +382 30 312 510\nEmail: reservations@hotelregaalis.svs.com",
		'rooms' : [{
		        'id' : '0',
		        'name' : "THE EMPERORS SUITE",
		        'price' : 17400,
		        'description' : 'Standard double room (25m2), out of which there are 72 connected rooms where it is possible to connect, which is ideal for accommodation of parents and children. 9 direct sea view 42 side sea view 55 park view',
		        'quantity' : 72
		    },
		    {
		        'id' : '1',
		        'name' : "THE DELUXE SUITE",
		        'price' : 13500,
		        'description' : 'Deluxe suite is a three-room, comfortable apartment which is consisted of living room, two bedrooms and two bathrooms. The apartments have direct sea view and park view. Maximal number of persons: four adults and two children.',
		        'quantity' : 4
		    }],
		'banquet' : [{
		        'id' : '0',
		        'name' : "The seventh hall",
		        'price' : 50000,
		        'description' : 'the area 150m2, has 120 seats (classroom), 150 seats (Theatat) and 50 seats (form II) and two smaller rooms, land 70m2, have the following capacity: 40 seats (Classroom), 50 seats (Theatat) and 25 seats (form II). In each room is modern audio-visual equipment PC and printer, projector, screen (Dimension 240 x 240), DVD, TV, video, flip chart, speakers and Internet access. There is the possibility of using fax, copier and printer equipment. In the immediate vicinity of these spaces is the lobby bar, an ideal place for a coffee break, and the Banketsaal, a place where their business lunch in a Erhohlung for all your senses transforms! Capacity: 80 seats',
		        'seating' : 150,
		        'quantity' : 3
		    }],
		'meeting' : [{
		        'id' : '0',
		        'name' : "Benedicts room",
		        'price' : 30000,
		        'description' : 'The Benedict Room is a multi-purpose room. The room is equipped with four rectangular tables, allowing multiple room configurations. Tables may be removed for discussion and prayer circles. The room is AV equipped with PC-compatible projection equipment. Dry erase board and easels are available.',
		        'seating' : 30,
		        'quantity' : 1
		    }],
		'restaurants' : [{
		        'id' : '0',
		        'name' : "La Gardenia",
		        'description' : 'All day dining, multi-cuisine, bistro style restaurant, offers the best of world cuisine.',
		        'quantity' : 100
		    },
		    {
		        'id' : '1',
		        'name' : "Chaarcoals",
		        'description' : 'Our pool side restaurant in Mangalore hotel offers the best of curries and kababs. Cane furniture, lush green landscape and the cool breeze flowing over the waters makes it an inviting option.',
		        'quantity' : 100
		    }]
	})

hotel.addHotel({
		'users' : ['0', '1'],
		'name' : "Hotel Seven seas",
		'description' : 'Lorem ipsum sit amet',
		'address' : "36/C Hosur road, Electronic city, Bangalore - 567200",
		'rooms' : [{
		        'id' : '0',
		        'name' : "The royal suite",
		        'price' : 10000,
		        'description' : 'Lorem ipsum sit amet',
		        'quantity' : 4
		    },
		    {
		        'id' : '1',
		        'name' : "Emperors suite",
		        'price' : 1000,
		        'description' : 'Lorem ipsum sit amet',
		        'quantity' : 10
		    }],
		'banquet' : [{
		        'id' : '0',
		        'name' : "The seven seas",
		        'price' : 10000,
		        'description' : 'Lorem ipsum sit amet',
		        'seating' : 400,
		        'quantity' : 1
		    }],
		'meeting' : [{
		        'id' : '0',
		        'name' : "The seven seas",
		        'price' : 10000,
		        'description' : 'Lorem ipsum sit amet',
		        'seating' : 30,
		        'quantity' : 1
		    }],
		'restaurants' : [{
		        'id' : '0',
		        'name' : "Fresho (A/C)",
		        'description' : 'Lorem ipsum sit amet',
		        'quantity' : 100
		    }]
	})

hotel.addHotel({
		'users' : ['0', '1'],
		'name' : "The song of the south",
		'description' : 'Lorem ipsum sit amet',
		'address' : "36/C Hosur road, Electronic city, Mangalore - 567201",
		'rooms' : [{
		        'id' : '0',
		        'name' : "The royal suite",
		        'price' : 10000,
		        'description' : 'Lorem ipsum sit amet',
		        'quantity' : 7
		    },
		    {
		        'id' : '1',
		        'name' : "Emperors suite",
		        'price' : 1000,
		        'description' : 'Lorem ipsum sit amet',
		        'quantity' : 1
		    }],
		'banquet' : [],
		'meeting' : [],
		'restaurants' : [{
		        'id' : '0',
		        'name' : "Fresho (A/C)",
		        'description' : 'Lorem ipsum sit amet',
		        'quantity' : 50
		    }]
	})

print "Hotels: done"
print db.database("hotels").data
print ""

# create reservation
reservations.addColumn("id")
reservations.addColumn("by")
reservations.addColumn("what")
reservations.addColumn("from")
reservations.addColumn("to")
reservations.addColumn("booking_time")
reservations.addColumn("confirmed")
reservations.addColumn("ended")
reservations.addColumn("comments")
reservations.addColumn("total_amount")
reservations.addColumn("quantity")
reservations.addColumn("reason")
reservations.addColumn("other")

print "Reservations: done"
print db.database("reservations").data
print ""

print "Utils: done"
print db.database("util").data
print ""