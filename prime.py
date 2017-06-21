x=int(raw_input())
y=int(raw_input())
flag=0
for j in range(x,y):
	if j<=2:
		print(j)
	else:
		i=2
		flag=0
		while i<j:
			if j%i==0:
				flag=flag+1
				break
			else:
				i=i+1
		if flag==0:
			print(j)
