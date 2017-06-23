x=raw_input()
z=list(x)
g=[]
z=z[::-1]
l=['a','e','i','o','u','A','E','I','O','U']
for i in range(len(z)):
	if z[i] in l:
		pass
	else:
		g.append(z[i])
print(''.join(z))
print(''.join(g))
