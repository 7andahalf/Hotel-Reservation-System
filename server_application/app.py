#!flask/bin/python

from flask import Flask, jsonify, abort
from router import query

'''
This script starts the server
Calls query method when any incoming connection comes
jsonifies the result and returns it
'''

app = Flask(__name__)
@app.route('/<name>', methods=['GET'])
def get_task(name):
	return jsonify(result=query(name))
app.run(host='0.0.0.0',debug=True)
