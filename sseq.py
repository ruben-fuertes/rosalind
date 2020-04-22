from sys import argv
file = open(argv[1]).read().lstrip('>').split('>')
seqs = []
for seq in file:
	seq = ''.join(seq.split()[1:])
	seqs.append(seq)
s = seqs[0]
t = seqs[1]
indices = []
j = 0
for base in t:
	for b in s[j:]:
		if base == b:
			indices.append(j+1)
			j+=1
			break
		j+=1
print(' '.join(list(map(lambda x: str(x), indices))))

