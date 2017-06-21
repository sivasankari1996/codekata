x=int(raw_input())
y=int(raw_input())
z=int(raw_input())
if x>y and x>z:
	print x, " is greater"
elif y>z and y>x:
	print y, "is greater"
else:
	print z, "is greater"
