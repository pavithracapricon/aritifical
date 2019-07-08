a=list(input())
if len(a)%2==0:
    a[int(len(a)/2)] ='*'
    a[int(len(a)/2)-1]='*'
else:
    a[int(len(a)/2)] ='*'
for i in range(0,len(a)):
    print(a[i],end='')
