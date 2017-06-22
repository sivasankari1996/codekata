x=raw_input()
y=raw_input()
l=len(x)
i=0
flag=0
for i in range(l):
	a,b=x[i],y[i]
	c=0
	j=i+1
	while j<l:
		if x[j]==a and y[j]==b:
			c=c+1
		j=j+1
	if c>=1:
		flag=flag+1
if flag!=0:
	print("true")
else:
	print("false")
