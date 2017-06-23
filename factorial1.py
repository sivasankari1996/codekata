import sys
x=int(raw_input())
fact=1
i=1
while i<=x:
	fact=fact*i
	sys.stdout.write(str(i))
	sys.stdout.write(" ")
	i=i+1
print  "\nThe factorial is", fact
