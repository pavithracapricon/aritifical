a,b=map(int,input().split())
a=a*b
for i in range(0,a+1):
 if(i**2==0):
  print("yes")
  break
else:
 print("no")
