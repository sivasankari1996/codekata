x=int(raw_input())
a=0
m=x
while x!=0:
	q=x/10
	r=x%10
	a=a*10+r
	x=q
if a==m:
	print('palindrome')
else:
	print('not a palindrome')
