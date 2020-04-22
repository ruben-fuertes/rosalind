from sys import argv
from functools import reduce
file = open(argv[1])
seqs = []
seq = ''
for line in file:
	if line.startswith('>'):
		if seq != '': seqs.append(seq)
		seq = ''
	else: seq+=line.rstrip()
seqs.append(seq)
seqsrev = list(map(lambda x: {x, x.replace('A', 't').replace('T', 'a').replace('C','g').replace('G','c').upper()[::-1]}, seqs))
buenas = []
malas = []
for i in range(len(seqsrev)):
	if seqsrev.count(seqsrev[i]) != 1:
		buenas.append(list(seqsrev[i])[0])
		buenas.append(list(seqsrev[i])[1])
	else: malas.append(seqs[i])
buenas = list(set(buenas))
def diff(a, b):
	difs = 0
	for i in range(len(a)):
		if a[i] != b[i]: difs+=1
	if difs == 1: return True
	else: return False
for seq in malas:
	for s in buenas:
		if diff(seq, s):
			print(seq+'->'+s)
			break
