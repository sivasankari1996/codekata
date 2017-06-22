x=raw_input()
y=len(x)
e=0
d=0
c=0
for i in range(y):
	if x[i].isalpha():
		c=c+1
	if x[i].isdigit():
		d=d+1
	e=e+1
print "Number of alphabets:" ,c
print "Number of numeric characters:", d
print "Number of characters:",e
