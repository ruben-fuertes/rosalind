from sys import argv
seq = open(argv[1]).read().rstrip().split()[1:]
seq = ''.join(list(map(lambda x: x.rstrip(), seq)))
print (seq)
cache = {1:seq[0]}
def kmp(seq):
	cadena = [0]
	for i in range(1, len(seq)):
		if cadena[i-1] == 0:
			if seq[i] != seq[0]:
				j = 0
				cadena.append(0)
				continue
			cadena.append(1)
			j = 1
		elif seq[i] == seq[j]:
			cadena.append(cadena[i-1]+1)
			cache[cadena[i-1]+1] = seq[:j+1]
			j += 1
		else:
			n = 0
			for a in cache:
				if a <= cadena[i-1] and cache[a] == seq[i-a+1:i+1]:
					if a > n: n = a
			j = n
			cadena.append(n)
	return list(map(lambda x: str(x),cadena))
out = open('out_kmp.txt', 'w')
for a in kmp(seq):
	out.write(a+' ')
print(cache)
