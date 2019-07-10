sbk2=int(input())
sbnt2=list(map(int,input().split()))
for p in range(len(sbnt2)-1):
     if(sbnt2[p]>sbnt2[p+1]):
           print(p)
           break
