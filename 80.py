s=input()
array=[]
if(s.isdigit()==True):
  for i in s:
    if(int(i)%2!=0):
      array.append(i)
print(*array)
