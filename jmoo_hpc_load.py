import pickle, pdb
from jmoo_core import *
from jmoo_properties import *
from mpi4py import MPI
import os, sys, inspect

with open('HpcData/whole.core', 'rb') as f:
    [core, tag] = pickle.load(f)

repeat_id = int(sys.argv[1])
Configurations["Universal"]["hpc"] = True
Configurations["Universal"]["repeat_id"] = repeat_id

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

for i, problem in enumerate(core.tests.problems):
    for algorithm in core.tests.algorithms:
        if i % 4 != rank: continue
        core.doSingleTest(problem, algorithm, repeat_id)
