from sys import argv
file = open(argv[1]).read().lstrip('>').split('>')
seqs = []
for seq in file:
	seq = ''.join(seq.split()[1:])
	seqs.append(seq)
s = seqs[0]
t = seqs[1]
i = -1
tv = 0
ts = 0
for base in s:
	i+=1
	if base == t[i]: continue
	elif base == 'A' and t[i] != 'G': tv += 1
	elif base == 'C' and t[i] != 'T': tv += 1
	elif base == 'G' and t[i] != 'A': tv += 1
	elif base == 'T' and t[i] != 'C': tv += 1
	else: ts += 1
print(ts/tv)
