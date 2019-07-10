n1=list(map(str,input()))
p1=t1=0
for i in range(0,len(n1)-1):
  q=n1[i]
  if int(q)!=0:
   for j in range(i+1,i+2):
    q=q+n1[j]
    if int(q)<27 and int(q)>0: p1=p1+1
    elif int(q)==0: p1=p1-1
    else: break
if p1!=1: t1=p%2
print(p1+t1+1)
