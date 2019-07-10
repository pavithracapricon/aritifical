jjj1,hhh1=map(int,input().split())
ff1=list(map(int,input().split()[:hhh1]))
kk1=[]
for i in ff1:
   if(i<=i+1):
     kk1.append(i)
print(kk1[hhh1-1])
