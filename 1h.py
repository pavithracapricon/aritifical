num2=int(input())
hk=list(map(int,input().split()[:num2]))
count=0
fp=[]
for i in range(0,num2+1):
   if(hk.count(i)>1):
      fp.append(i)
if(len(fp)==0):
   print("unique")
ew=sorted(fp)
print(' '.join(map(str,ew)))
