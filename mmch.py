from sys import argv
from math import factorial
file = open(argv[1])

seq = ''
for line in file:
	line = line.rstrip().upper()
	if not line.startswith('>'): seq+=line

# seq = 'CAGCGUGAUCACCAGCGUGAUCAC'

def maxmatches(sec):
    '''This function takes a RNA sequence and
    calculates the number of different max matches
    that can be made'''
    A = sec.count('A')
    U = sec.count('U')
    G = sec.count('G')
    C = sec.count('C')
    print(A,U,G,C)
    return factorial(max(A,U))//factorial(max(A,U)-min(A,U)) * factorial(max(G,C))//factorial(max(G,C)-min(G,C))

print (maxmatches(seq))
