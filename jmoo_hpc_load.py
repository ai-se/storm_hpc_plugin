import pickle, pdb
from jmoo_core import *

import os, sys, inspect

with open('HpcData/whole.core', 'rb') as f:
    [core, tag] = pickle.load(f)

repeat_id = int(sys.argv[1])


for problem in core.tests.problems:
    for algorithm in core.tests.algorithms:
        core.doSingleTest(problem, algorithm, repeat_id)
