x=int(raw_input())
flag=0
if x<=2:
	print('prime')
else:
	i=2
	while i<x:
		if x%i==0:
			flag=flag+1
		else:
			break
		i=i+1
	if flag==0:
		print('prime')
	else:
		print('not a prime')
