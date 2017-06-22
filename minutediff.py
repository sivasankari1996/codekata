def minu(a):
	r=a.split(':')
	i=int(r[0])*60+int(r[1])
	return i
x=raw_input()
y=raw_input()
g=minu(x)
h=minu(y)
d=h-g
print "The difference is:",d
