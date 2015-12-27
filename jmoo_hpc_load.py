import pickle
import sys

with open('hpc_dumps/tmp_jmoo_core_obj','rb') as f:
    [core,tag] = pickle.load(f)

index = int(sys.argv[1])
if index > len(core.tests.algorithms):
    print 'no!no!no! index error at hpc job submitting'
    exit(0)

core.tests.algorithms = core.tests.algorithms[index:index+1]
core.doTests_hpc()
core.doReports(tag)
