from sys import argv
file = open(argv[1]).read().split()
n = int(file[0])
GCs = float(file[1])
seq = file[2]
lon = len(seq)
print( 1- (1- (GCs/2)**(seq.count('C')+seq.count('G'))* ((1-GCs)/2)**(seq.count('T')+seq.count('A')) )**n )
