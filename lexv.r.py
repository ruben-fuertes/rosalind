from sys import argv
input = open(argv[1]).read().strip('\n').split('\n')

alphabet, n = input[0].split(), int(input[1])

def generate(n, h=""):
    print (h)
    if n == 0:
        return
    for c in alphabet:
        generate(n-1, h+c)

generate(n)
