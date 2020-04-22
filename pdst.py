from sys import argv
fastafile = open(argv[1])
seq = ''
seqs = []
for line in fastafile:
	line = line.rstrip()
	if line.startswith('>'):
		seqs.append(seq)
		seq = ''
		continue
	else: seq+=line
seqs.append(seq)
seqs = seqs[1:]
def dist(a, b):
	distancia = float(0)
	for i in range(len(a)):
		if a[i] != b[i]: distancia +=1
	return distancia/len(a)
for i in range(len(seqs)):
	a = []
	for j in range(len(seqs)):
		a.append(str(dist(seqs[i], seqs[j])))
	print(' '.join(a))
