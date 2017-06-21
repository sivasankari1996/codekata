x=int(raw_input())
a=0
b=1
i=0
while i<x:
	if i<=1:
		print i
	else:
		c=a+b
		a=b
		b=c
		print c
	i=i+1
