from sys import argv
file = open(argv[1]).read().rstrip().split('\n')
total = int(file[0])
solos = total - len(set(open(argv[1]).read().split()[1:]))
edges = list(map(lambda x: set(x.split()),file[1:]))
tree = []
print(solos)
while len(edges) != 0:
	for edge in edges:
		i = 0
		edge = edges.pop(0)
		if edge in edges: continue
		for e in edges:
			if len(e) + len(edge) != len(e.union(edge)):
				edges.append(e.union(edge))
				i = 1
				break
		if i == 0 and edge not in tree: tree.append(edge)
print(tree)
print(len(tree) + solos - 1)
