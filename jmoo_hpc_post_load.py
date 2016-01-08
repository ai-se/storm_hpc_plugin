import pickle, pdb
from jmoo_core import *
import jmoo_properties

import os, sys, inspect

with open('HpcData/whole.core', 'rb') as f:
    [core, tag] = pickle.load(f)

jmoo_properties.Configurations["Universal"]["hpc"] = True
core.merging_results_hpc()
core.doReports(tag)
