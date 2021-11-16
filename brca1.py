#program to calculate the GC content

gene = open("sequence.txt", "r")

#setting values to zero

g = 0;
a = 0;
c = 0;
t = 0;

#skip first line of header
gene.readline()

for line in gene:
	line = line.lower()
	for char in line:
		if char == "g":
			g+=1
		if char == "a":
			a+=1
		if char == "c":
			c+=1
		if char == "t":
			t+=1

print("number of g's" + str(g))
print("number of g's" + str(c))
print("number of g's" + str(a))
print("number of g's" + str(t))

gc = (g+c+0.) / (a+t+c+g+0.)

print("gc content : " + str(gc))