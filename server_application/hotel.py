

from db import database

'''
Structure of hotels database

id  : users       : name : address : rooms : banquet : meeting : restaurants : description
str   list of str   str    str       c.list  c.list    c.list    c.list      : str

Structure of rooms:
rooms = [
    {
        'id' = '1',
        'name' = "The royal suite",
        'price' = 10000,
        'description' = 'Lorem ipsum sit amet'
        'quantity' = 4
    },
    {
        'id' = '2',
        'name' = "Emperors suite",
        'price' = 1000,
        'description' = 'Lorem ipsum sit amet'
        'quantity' = 10
    }
]

Structure of banquet:
banquet = [
    {
        'id' = '1',
        'name' = "The seven seas",
        'price' = 10000,
        'description' = 'Lorem ipsum sit amet',
        'seating' = 400,
        'quantity' = 1
    }
]

Structure of meeting:
meeting = [
    {
        'id' = '1',
        'name' = "The seven seas",
        'price' = 10000,
        'description' = 'Lorem ipsum sit amet',
        'quantity' : 1,
        'seating' = 30
    }
]

Structure of restaurants:
restaurants = [
    {
        'id' = '1',
        'name' = "Fresho (A/C)",
        'description' = 'Lorem ipsum sit amet'
        'quantity' = 100
    }
]


'''

# Adds a hotel to the database. needs data as a dictionary. ID will be automatically generated
def addHotel(data):
    hotels = database("hotels")
    util = database("util")
    data['id'] = str(util.get("name","num_hotels")[0]['value'])
    if hotels.insert(data):
    	util.change("name","num_hotels","value",util.get("name","num_hotels")[0]['value']+1)
    	return True
    else:
    	return False

# Gets all hotels in the database
def getAllHotels():
    return database("hotels").rows

# Gets a particular hotel from the database
def getHotel(name,value):
	return database("hotels").get(name,value)

# Changes something is the entry
def changeHotel(name,value,name2,value2):
	return database("hotels").change(name,value,name2,value2)

# Gets a particular value of the hotel
def getData(id,value):
	return database("hotels").get("id",id)[0][value]

# Truncates sensetive information before sending data to the user
def secureData(data):
    data.pop('users',None)
    return data

# Testcases    
'''
if __name__ == "__main__":
    #print addHotel({'users':[1,2],'banquet':[],'rooms':[["hola"],["hola2"]],'address':["bang"],'restaurants':[123],'meeting':[],'name':"the seven seas"})
    #print getData(1,'banquet')
    #print getHotel('id','1')
    print database("hotels").data
'''




