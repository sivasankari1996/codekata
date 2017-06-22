x=raw_input()
y=len(x)
dict={'I':'1','V':'5','X':'10','L':'50','C':'100'}
c=0
if y==1:
	print(dict[x])
else:
	for i in range(0,len(x),2):
		if x[i] in dict.keys():
			if int(dict[x[i+1]])>int(dict[x[i]]):
				c=c+(int(dict[x[i+1]])-int(dict[x[i]]))
			else:
				c=c+int(dict[x[i]])+int(dict[x[i+1]])
		else:
			print('undefined')
	print(c)
