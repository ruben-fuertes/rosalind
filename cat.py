from sys import argv
seq = open(argv[1]).read().rstrip().split()[1:]
seq = ''.join(list(map(lambda x: x.rstrip(), seq)))
def match(a,b):
	if a == 'A' and b == 'U': return 1
	elif a == 'U' and b == 'A': return 1
	elif a == 'G' and b == 'C': return 1
	elif a == 'C' and b == 'G': return 1
	else: return 0
cache = {}
def Pcount(seq):
	if seq in cache: return cache[seq]
	if len(seq) == 2:
		return match(seq[0], seq[1])
	elif seq == '': return 1
	tmp = []
	for i in range(1, len(seq), 2):
		tmp.append(Pcount(seq[1:i])*match(seq[0],seq[i])*Pcount(seq[i+1:]))
	cache[seq] = sum(tmp)
	return(cache[seq])
print(Pcount(seq)%1000000)
