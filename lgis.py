#file = open('rosalind_lgis.txt').read().split()
file = [4,2,5,1,3,6,0,10,7,9,8]
secuence = []
for a in file:
	secuence.append(int(a))
tuple(secuence)
d = {}
i = 0
ev = [float('inf')]
for num in secuence:
	num
	if num < ev[-1]:
		ev.append(num)
		d[num] = [(float('inf'),0)]
		currpos = i
		for currnum in secuence[i:]:
			currpos += 1
			if currnum > num and currnum < d[num][-1][0]:
				if d[num][0] == (float('inf'),0): d[num].pop()
				d[num].append((currnum,currpos))
	i+=1
for num in d:
	a = len(d[num])
	for i in range(a):
		actual = d[num].pop(0)
		nactual = actual[-2]
		pos = actual[-1]
		currpos = pos
		for currnum in secuence[pos:]:
			currpos += 1
			if (currnum > nactual and currnum < d[num][-1][-2]) or :
				d[num].append(tuple(list(actual[:-1])+[currnum,currpos]))


print (d)
