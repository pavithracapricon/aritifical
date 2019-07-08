b1,b2=map(int,input().split())
maximum=max(b1,b2)
while(1):
   if(maximum%b1==0 and maximum%b2==0):
          print(maximum)
          break
   maximum+=1
