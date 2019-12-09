def check_qstat(inputname):
	return 'RUNNING'

def getStep(Path):
	'''
	Takes absolute path from runoutput file and returns the current step.
	If step is 0 then the runoutput file does not exist or is still initializing.
	'''
	return 5

def getRunTime(Path):
	'''
	Takes absolute path of runoutput file and returns the total runtime of the test.
	If runtime is 0 then process exited prematurely. Returns runtime in seconds.
	'''
	return 100000


def calculateHeuristics(Path):
	'''
	Takes absolute path of output directory and parses files to determine whether job was successful.
	'''
	return {"breathingratio":1.1}
