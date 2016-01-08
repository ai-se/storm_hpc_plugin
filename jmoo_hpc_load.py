import pickle, pdb
from jmoo_core import *
from jmoo_properties import *
import os, sys, inspect

with open('HpcData/whole.core', 'rb') as f:
    [core, tag] = pickle.load(f)

repeat_id = int(sys.argv[1])
Configurations["Universal"]["hpc"] = True
Configurations["Universal"]["repeat_id"] = repeat_id

for problem in core.tests.problems:
    for algorithm in core.tests.algorithms:
        core.doSingleTest(problem, algorithm, repeat_id)
