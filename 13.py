n=int(input("enter number"))
if n<=1000:
 for i in range(2,n):
  if(n % i)==0:
   print("yes")
  else:
   print("no")
