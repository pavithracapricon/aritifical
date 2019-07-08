N= int(input("Please Enter any Number: "))    
Reverse = 0    
while(N> 0):    
  Reminder = N %10    
  Reverse = (Reverse *10) + Reminder    
  N = N //10    
print("\n Reverse of entered number is = %d" %Reverse) 
