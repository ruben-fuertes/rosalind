from sys import argv
fastafile = open(argv[1])
seq = ''
seqs = []
for line in fastafile:
	if line.startswith('>'):
		seqs.append(seq)
		seq = ''
	else: seq += line.rstrip()
seqs.append(seq)
seqA = seqs[1]
seqB = seqs[2]

def lssm(s, t):
    '''This function takes two DNA seqs and finds the
    longest shared subsequence between them'''
    # Create indexes for dinamic programming solution
    ind = [[0 for i in range(len(s) + 1)] for i in range(len(t) + 1)]

    # Loop through the bases of the sequences and check if they match
    # if they do, update the matrix
    for i, x in enumerate(t):
        for j, y in enumerate(s):
            if x == y:
                ind[i+1][j+1] = ind[i][j] + 1
            else:
                ind[i+1][j+1] = max(ind[i][j+1], ind[i+1][j])

    # Reconstitute the string from the indexes
    mot = ''
    a,b = len(t),len(s)
    while a!=0 and b!=0:

        if ind[a][b] == ind[a-1][b]:
            a -= 1

        elif ind[a][b] == ind[a][b-1]:
            b -= 1

        else:
            mot += t[a-1]
            a -= 1
            b -= 1

    return mot[::-1]


print(lssm(seqA, seqB))
