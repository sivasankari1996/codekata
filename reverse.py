x=int(raw_input())
y=len(str(x))
a=0
while x!=0:
	q=x/10
	r=x%10
	a=a*10+r
	x=q
print(a)
	
