x=int(raw_input())
y=int(raw_input())
for i in range(x,y):
	y=len(str(i))
	z=int(i)
	s=0
	m=z
	while z!=0:
		q=z/10
		r=z%10
		s=s+(r**y)
		z=q
	if s==m:
		print(i)
