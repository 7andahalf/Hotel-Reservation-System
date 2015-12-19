import urllib, json

'''
This module can be used to connect to the API server for the exachange
of information

HOW TO USE:

1) with no username and password:

	link.request(data)

		where data can be following:

		for the task forgot password: u...forgot_pass.username
		for verification of sec que: u...forgot_pass_verify.username,secans
		etc

2) With username ans password

	create an object like this:

	server = link(<username>, <password>)

	# to test connection to server
	link.testConnection() #returns True or False

	# to test username and password
	try:
		server.login()
	except:
		when login fails take appropriate action

	# to request some task

	data = server.req(<task_name>,<var1>,<var2>,.....)
	for example: data = server.req('get_user_details')
				 data = server.req('get_hotel_by_id','1')
				 etc.

	link.request(data) can also be used with appropriate formatting of data
	so as to include username passw tasks etc. inside it
'''

class link:
	# Address of the server
	server = "http://localhost:5000/"
	mode = 'a'

	# Initialize and see if connection to server is possible
	def __init__(self,usern,passw):
		self.username = usern
		self.password = passw

	# Logs in raises exceptions if logging in fails
	def login(self):
		if link.testConnection():
			if link.request(self.mode+'.'+self.username+'.'+self.password+'..')[0] == 'successful login':
				self.head = self.mode+'.'+self.username+'.'+self.password+'.'
				return True
			raise ValueError('Login Failed')
		raise ValueError('Connection Failed')

	# Requests can be made from this method
	def req(self,task,*params):
		if link.testConnection() and self.login():
			return link.request(self.head+task+'.'+"".join([","+str(i) for i in params])[1:])
		raise ValueError('Connection Failed')

	# Used to test connection to the server
	@staticmethod
	def testConnection():
		try:
			json.load(urllib.urlopen(link.server+'....'))
			return True
		except:
			return False

	# This request method takes in raw parameters
	# Request can be done like request("u.usern.passw.get_user_details.")
	@staticmethod
	def request(data):
		if link.testConnection:
			return makeStrings(json.load(urllib.urlopen(link.server+data))['result'])
		raise ValueError('Connection Failed')

# JSON returns the elements in unicode format, this function recursively converts
# all elements into strings.
# from http://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-ones-from-json-in-python
def makeStrings(thing):
	if isinstance(thing, dict):
		return dict([(makeStrings(key), makeStrings(value)) for key, value in thing.iteritems()])
	elif isinstance(thing, list):
		return [makeStrings(element) for element in thing]
	elif isinstance(thing, unicode):
		return thing.encode('utf-8')
	else:
		return thing

# Testcases
'''
if __name__ == "__main__":
	server = link('ruby','bowbow')
	
	if not link.testConnection():
		print "Connection failed"
		exit()

	try:
		server.login()
	except:
		print "Login credentials don't match"
		exit()

	# Query 1
	data = server.req('get_user_details')
	print 'Users details :'
	for i in data:
		print '\t' + i + ':' + data[i]

	# Query 2
	data = server.req('get_all_hotels')
	print "\n All hotels"
	for i in data:
		print ""
		for j in i:
			print '\t' + j + ':' + str(i[j])

	# Query 3
	data = server.req('get_hotel_by_id',0)[0]
	print '\nParticular hotel :'
	for i in data:
		print '\t' + i + ':' + str(data[i])
'''











