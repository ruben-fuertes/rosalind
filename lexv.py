from sys import argv
from itertools import product
letras = open(argv[1]).read().split('\n')[0].split()
n = int(open(argv[1]).read().split('\n')[1])
numeros = []
for i in range(len(letras)+1):
	numeros.append(i)
nperms = list(sorted(list(product(numeros, repeat=n))))
lperm = []
print(nperms)
for perm in nperms:
	perm = nperms.pop(0)
	print(perm)
	a = []
	for n in list(perm):
		if n == 0: continue
		a.append(n)
	nperms.append(a)
print (nperms)
for perm in sorted(nperms):
	l = []
	for n in list(perm):
		l.append(letras[n-1])
	if "".join(l) not in lperm: lperm.append(''.join(l))
print('\n'.join(lperm[1:]))
