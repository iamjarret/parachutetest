from connect import tests, runs, Run

from os import path, mkdir, system
import pygit2
from jinja2 import Template
import glob

for x in tests.find({'built':False,'finished':False}):
	#make directory
	targetpath = path.abspath(path.join("./outputs/",x['testname']))
	mkdir(targetpath)

	#download
	pygit2.clone_repository("https://github.com/b2tine/FronTierCpp.git",targetpath,
		checkout_branch=x['branch'])
	tests.update({'testname':x['testname']},{'$set':{'downloaded':True}})

	#build
	status = system("cd %s && ./build -d"%targetpath)
	if status != 0:
		tests.update({'testname':x['testname']},{'$set':{'details':"BUILD ERROR", 'finished':True}}) #build error
		continue
	else:
		tests.update({'testname':x['testname']},{'$set':{'built':True}}) #build success

	#make input dir
	inputdir = path.join(targetpath,"parachute/",x['testname'])
	mkdir(inputdir)

	#copy inputs and create documents
	inputs = []
	for document in glob.glob(path.join('./inputs/',x['testgroup'])+'/*'):
		docname = path.basename(document)
		with open(document, 'r') as f:
			template = Template(f.read())
		inputfile = template.render(**x['data'])
		name = "%s-parachute-%s-np1"%(x['testname'],docname)
		run = Run(name, inputfile, x['testname'])
		inputs.append(run)

		#copy to location
		inputwritedir = path.join(inputdir, docname)
		with open(inputwritedir, 'w') as w:
			w.write(inputfile)
	runs.insert(inputs)
		
	#submit jobs
	parachutepath = path.join(targetpath,"parachute/")
	print(parachutepath)
	status = system("cd %s && ./qrun-inputdir3d %s 1 1 1 && cd .."%(parachutepath,x['testname']))
	if status==0:
		tests.update({'testname':x['testname']},{'$set':{'submitted':True,'running':True}}) #submitted success
	else:
		tests.update({'testname':x['testname']},{'$set':{'details':"SUBMISSION ERROR", 'finished':True}}) #submission error


