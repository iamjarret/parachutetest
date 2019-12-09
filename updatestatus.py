'''
run every 30 minutes

This should check qrun, decide what tasks are done, and update all relevant data.
'''
from connect import tests, runs, Run
from statustools import check_qstat, getStep, getRunTime, calculateHeuristics

from os import path, system
import os

#freeze qstat data in qstat.xml
qstat = system("qstat -xml > qstat.xml")

for x in runs.find({"finished": {"$ne" : True}}):
	inputname = "out-"+"-".join(x['name'].split("-")[3:-1])
	print(x['name'])
	print(inputname)
	absolutePath = path.abspath(path.join("./outputs/", x['testname'], "parachute", "out-" + x['testname'] + "-p111",inputname))
	print(absolutePath)
	if !os.path.exists(absolutePath):
		print("doesn't exist")
	break
	 
	#update status with running/waiting/finished
	#if finished read run.output 
	#Get execution time, heuristics, timestep and update finished = True 




#function parseRunOutputBasic(Path) returns dict of basic data to be added
	
#function parseRunOutputHeuristic(Path) returns dict of heuristic data to be added
