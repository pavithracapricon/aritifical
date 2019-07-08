R,R2=map(str,input().split())
if(len(R)!=len(R2)):
   print("no")
else:
   S1=[R.count(a) for a in R]
   T1=[R2.count(a) for a in R2]
if(S1==T1):
   print("yes")
else:
   print("no")
