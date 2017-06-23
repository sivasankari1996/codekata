def workingday(a):
  dict={'sunday':'0','monday':'1','tuesday':'1','wednesday':'1','thursday':'1','friday':'1','saturday':'1'}	
  if a in dict.keys():
    if dict[a]=='1':
      return 'true'
    else:
      return 'false'
  else:
   print("please enter valid day")
x=str(raw_input())
d=workingday(x)
print(d)
