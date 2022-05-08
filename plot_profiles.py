import pylab
import modeller

def r_enumerate(seq):
    """Enumerate a sequence in reverse order"""
    # Note that we don't use reversed() since Python 2.3 doesn't have it
    num = len(seq) - 1
    while num >= 0:
        yield num, seq[num]
        num -= 1

def get_profile(profile_file, seq):
    """Read `profile_file` into a Python array, and add gaps corresponding to
       the alignment sequence `seq`."""
    # Read all non-comment and non-blank lines from the file:
    f = open(profile_file)
    vals = []
    for line in f:
        if not line.startswith('#') and len(line) > 10:
            spl = line.split()
            vals.append(float(spl[-1]))
    # Insert gaps into the profile corresponding to those in seq:
    for n, res in r_enumerate(seq.residues):
        for gap in range(res.get_leading_gaps()):
            vals.insert(n, None)
    # Add a gap at position '0', so that we effectively count from 1:
    vals.insert(0, None)
    return vals

e = modeller.Environ()
a = modeller.Alignment(e, file='query-7dwzA.ali')

template = get_profile('7dwzA.profile', a['7dwzA'])
for i in range(9):
    model = get_profile('query.B9999000' + str(i+1) + '.pdb', a['query.B9999000' + str(i)])
    # Plot the template and model profiles in the same plot for comparison:
    pylab.figure(1, figsize=(10,6))
    pylab.xlabel('Alignment position')
    pylab.ylabel('DOPE per-residue score')
    pylab.plot(model, color='red', linewidth=2, label='Model')
    pylab.plot(template, color='green', linewidth=2, label='Template')
    pylab.legend()
    pylab.savefig('query.B9999000' + str(i+1) + '.png', dpi=65)

for i in range(10, 99):
    model = get_profile('query.B999900' + str(i+1) + '.pdb', a['query.B999900' + str(i)])
    # Plot the template and model profiles in the same plot for comparison:
    pylab.figure(1, figsize=(10,6))
    pylab.xlabel('Alignment position')
    pylab.ylabel('DOPE per-residue score')
    pylab.plot(model, color='red', linewidth=2, label='Model')
    pylab.plot(template, color='green', linewidth=2, label='Template')
    pylab.legend()
    pylab.savefig('query.B999900' + str(i+1) + '.png', dpi=65)

model = get_profile('query.B99990100.pdb', a['query.B99990100'])
# Plot the template and model profiles in the same plot for comparison:
pylab.figure(1, figsize=(10,6))
pylab.xlabel('Alignment position')
pylab.ylabel('DOPE per-residue score')
pylab.plot(model, color='red', linewidth=2, label='Model')
pylab.plot(template, color='green', linewidth=2, label='Template')
pylab.legend()
pylab.savefig('query.B99990100.png', dpi=65)
