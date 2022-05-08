from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='7dwz', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='7dwzA', atom_files='7dwz.pdb')
aln.append(file='query.ali', align_codes='query')
aln.align2d(max_gap_length=50)
aln.write(file='query-7dwzA.ali', alignment_format='PIR')
aln.write(file='query-7dwzA.pap', alignment_format='PAP')










