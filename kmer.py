from sys import argv
from itertools import product
n = 4
seq = ''.join(open(argv[1]).read().split()[1:])
p = list(map(lambda x: "".join(x), list(product('ACTG',repeat=n))))
d = {}
for a in p:
	d[a] = 0
i = 0
for base in seq:
	if len(seq[i:i+n]) == n : d[seq[i:i+n]] += 1
	i += 1
solution = ''
for a in sorted(d):
	solution += str(d[a])+' '
print(solution)
