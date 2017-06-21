x=raw_input()
y=len(x)
z=int(x)
s=0
m=z
while z!=0:
	q=z/10
	r=z%10
	s=s+(r**y)
	z=q
if s==m:
	print('Armstrong number')
else:
	print('Not a armstrong number')
