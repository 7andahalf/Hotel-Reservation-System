

from db import database

'''
Structure of users database

id  : username : password : fname : lname : gender : mobile : secque : secans
str   str        str        str     str     str      str      str      str

'''

# Adds a user to the database needs data as a dictionary. ID will be automatically generated
def addUser(data):
    users = database("users")
    util = database("util")
    if not data.has_key("username") or len(users.get("username", data["username"])) > 0:
    	return False
    data['id'] = str(util.get("name","num_users")[0]['value'])
    if users.insert(data):
    	util.change("name","num_users","value",util.get("name","num_users")[0]['value']+1)
    	return True
    else:
    	return False

# Verifies credentials of the user
def authUser(usern, passw):
	users = database("users")
	if len(users.get("username",usern)) == 1 and users.get("username",usern)[0]['password'] == passw:
		return True
	else:
		return False

# Gets data of users
def getUser(name, value):
	return database("users").get(name,value)

# Gets all users
def getAllUsers():
	return database("users").rows

# Truncates sensetive information before sending data to the user
def secureData(data):
    data.pop('password',None)
    data.pop('secans',None)
    data.pop('secque',None)
    return data

# Retrives the security question
def secQue(usern):
    d = getUser('username', usern)
    if len(d) > 0:
        return d[0]['secque']
    return []

# Verifies security answer
def verSecAns(usern, ans):
    d = getUser('username', usern)
    if len(d) > 0 and getUser('username', usern)[0]['secans'] == ans:
        return getUser('username', usern)[0]['password']
    else:
        return "Wrong answer"

# Test cases
'''
if __name__ == "__main__":
    print addUser({'username': 'vinay4', 'mobile': '1234567890', 'gender': 'male', 'lname': 'C K', 'secans': 'ruby', 'fname': 'Vinay', 'secque': 'dog', 'password': '123'})
	print authUser('vqinay','1232')
    print database("users").data
    print secQue('vinaay')
    print verSecAns('vinay','rubya')
'''



