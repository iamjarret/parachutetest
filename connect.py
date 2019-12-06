from pymongo import MongoClient
import os
import datetime
import hashlib

DBPASS = os.environ.get('DBPASS')
client = MongoClient('mongodb+srv://parachutetest:%s@cluster0-glh6n.azure.mongodb.net/test?retryWrites=true&w=majority'%DBPASS)

parachutetest = client.parachutetest

tests = parachutetest.tests
runs = parachutetest.runs


class Test(dict):
	def __init__(self, branchname, saveVTK, testgroup, timesteps, maxtime):
		self['submitted'] = False
		self['finished'] = False
		self['branch'] = branchname
		self['data'] = {'timesteps': timesteps, 'maxtime': maxtime}
		self['built'] = False
		self['date'] =  datetime.datetime.now()
		self['running'] = False
		self['testgroup'] = testgroup
		self['testname'] = hashlib.sha256(datetime.datetime.now().__str__().encode('ascii')).hexdigest()[0:10]
		self['saveVTK'] = saveVTK
		self['downloaded'] = False
		
class Run(dict):
	def __init__(self, name, inputfile, testname):
		self['name'] = name
		self['inputfile'] = inputfile
		self['testname'] = testname
		

'''
t = Test("master", True, "all", 1000, 3)
print(t)


for x in tests.find():
	print(x.keys())
	
	for run in x['runs']:
		objectid = runs.find_one({'_id':run})
		print(objectid)

'''
