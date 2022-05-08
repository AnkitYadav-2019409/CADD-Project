file1 = open('spike.fasta', 'r')
lines = []
for x in file1:
    lines.append(x.strip())
seq = list(lines[1])
# print(lines)

change = {18: 'F', 20: 'N', 26: 'S', 138: 'Y', 190: 'S', 417: 'N', 484: 'K', 501: 'Y', 614: 'G', 655: 'Y', 1027: 'I', 1176: 'F'}
for i in range(0, len(seq)):
    if(i+1 in change):
        print(seq[i])
    if(i+1 in change):
        seq[i] = change[i+1]
# print(seq)
modified = ''.join(seq)
print(modified)