x=raw_input()
y=list(x)
z=len(y)
for i in range(0,z,2):
	y[i],y[i+1]=y[i+1],y[i]
print(''.join(y))
	
