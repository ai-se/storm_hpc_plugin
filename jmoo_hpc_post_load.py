import pickle, pdb
from jmoo_core import *

import os, sys, inspect

with open('HpcData/whole.core', 'rb') as f:
    [core, tag] = pickle.load(f)

core.merging_results_hpc()
core.doReports(tag)
