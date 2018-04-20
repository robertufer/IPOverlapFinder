import netaddr
from intervaltree import Interval, IntervalTree


comparefilea = open('outputaddressesA.txt', 'r')
comparefileb = open('outputaddressesB.txt', 'r')

lista = []
listb = []

# load up comparison files by creating list of tuples 
for line in comparefilea:
	line = tuple(a for a in line.split() if a)
	lista.append(line)
#print(lista)

for line in comparefileb:
	line = tuple(b for b in line.split() if b)
	listb.append(line)
#print(listb)


# form interval trees out of tuple lists
tree1 = IntervalTree.from_tuples(lista)
tree2 = IntervalTree.from_tuples(listb)


# search method, by picking each range within B and checking if it overlaps with the A tree 
for e in tree2:																											# show true / false if overlap
	print(str(e in tree1) + "\t" + str(netaddr.IPAddress(e[0])) + '\t' + str(netaddr.IPAddress(e[1])))


comparefilea.close()
comparefileb.close()