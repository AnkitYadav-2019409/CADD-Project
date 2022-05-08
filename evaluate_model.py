from modeller import *
from modeller.scripts import complete_pdb

log.verbose()    # request verbose output
env = Environ()
env.libs.topology.read(file='$(LIB)/top_heav.lib') # read topology
env.libs.parameters.read(file='$(LIB)/par.lib') # read parameters

# for 1 digit
for i in range(9):
    # read model file
    mdl = complete_pdb(env, 'query.B9999000' + str(i+1) + '.pdb')
    # Assess with DOPE:
    s = Selection(mdl)   # all atom selection
    s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='query.B9999000' + str(i+1) + '.profile',
                normalize_profile=True, smoothing_window=15)

for i in range(10, 99):
    # read model file
    mdl = complete_pdb(env, 'query.B999900' + str(i+1) + '.pdb')
    # Assess with DOPE:
    s = Selection(mdl)   # all atom selection
    s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='query.B999900' + str(i+1) + '.profile',
                normalize_profile=True, smoothing_window=15)

# Doing for 100th model separate because it is 3 digit
mdl = complete_pdb(env, 'query.B99990100.pdb')
# Assess with DOPE:
s = Selection(mdl)   # all atom selection
s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='query.B99990100.profile',
            normalize_profile=True, smoothing_window=15)
