s = int(input("Enter the start")) 
e = int(input("Enter the end")) 
for num in range(s, e + 1):  
  if num % 2 == 0: 
   print(num, end = " ")
