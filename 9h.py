t1=int(input())
s1=list(map(int,input().split()))
m1=max(s)
a,b=0,0
for i in range(0,len(s1)-1):
  for j in range(i+1,len(s1)):
    if abs(s1[i]+s1[j])<m1:
      a,b=s1[i],s1[j]
      m1=abs(a+b)
print(a,b)
