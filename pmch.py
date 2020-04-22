from sys import argv
from math import factorial
file = open(argv[1])
seq = ''
for line in file:
	line = line.rstrip()
	if not line.startswith('>'): seq+=line
def perfectmatches(sec):
	return factorial(sec.count('A'))*factorial(sec.count('G'))
print(perfectmatches(seq))
