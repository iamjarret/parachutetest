doc = '''
starttest.py is a command line procedure to initiate a test.

It adds the test to our MongoDB database, giving it a unique
name.

python teststart.py BRANCHNAME testgroupo MAXSTEPS MAXTIME
'''
import argparse
import github
import os

from connect import Test, tests
from errors import UnknownBranchName, UnknownTestGroup

parser = argparse.ArgumentParser(description = doc)
parser.add_argument("branchname", type=str, help="The github branch to test.")
parser.add_argument("testgroup", type=str, help="Required group of inputs to use for test. 'all' is default.") 
parser.add_argument("maxsteps", type=int, help="Max number of steps to use for runs.")
parser.add_argument("maxtime", type=float, help="Max time to use for runs.")
parser.add_argument("-s", "--saveVTK", action="store_true",
                    help="Optional argument to save VTK output.")
args = parser.parse_args()

#decide if branch is a valid name
g = github.Github()
repo=g.get_repo("b2tine/FronTierCpp")
if args.branchname not in [x.name for x in repo.get_branches()]:
	raise UnknownBranchName

#decide if group of inputs is valid
listofgroups = [x[0] for x in [x[1] for x in os.walk("./inputs")] if x]
if args.testgroup not in listofgroups:
	raise UnknownTestGroup

test = Test(args.branchname, args.saveVTK, args.testgroup, args.maxsteps, args.maxtime)
tests.insert(test)
