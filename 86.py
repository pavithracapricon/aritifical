k=list(input())
ink=[]
for j in k:
   if j not in ink:
      ink.append(j)
if k==ink:
   print("Yes")
else:
   print("No")
