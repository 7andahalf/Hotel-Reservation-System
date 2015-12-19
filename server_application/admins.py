from db import database

'''
Structure of admins database

id  : username : password : name :  permissions
str   str        str        str     list of ints

'''

# Adds an admin to the database needs data as a dictionary. ID will be automatically generated
def addAdmin(data):
    admins = database("admins")
    util = database("util")
    if not data.has_key("username") or len(admins.get("username", data["username"])) > 0:
    	return False
    data['id'] = str(util.get("name","num_admins")[0]['value'])
    if admins.insert(data):
    	util.change("name","num_admins","value",util.get("name","num_admins")[0]['value']+1)
    	return True
    else:
    	return False

# Verifies credentials of the admin
def authAdmin(usern, passw):
	admins = database("admins")
	if len(admins.get("username",usern)) == 1 and admins.get("username",usern)[0]['password'] == passw:
		return True
	else:
		return False

# Gets admin details
def getAdmin(name, value):
	return database("admins").get(name,value)

# Gets the permissions available to the admin
def getPerm(usern):
    return database("admins").get("username",usern)[0]['permissions']

# Truncates sensetive information before sending data to the user
def secureData(data):
    data.pop('password',None)
    return data

# Test cases
'''
if __name__ == "__main__":
    print database("admins").data
    print addAdmin({'username': 'vinay2', 'password': '123', 'name': 'vinay', 'permissions': [1,2,3]})
    print authAdmin('vinay11','123')
    print getUser('id',0)
'''
