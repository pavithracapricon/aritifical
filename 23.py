def smallest(arr,n): 
   min = arr[0] 
   for i in range(1, n): 
     if arr[i] < min: 
      min = arr[i] 
   return min
   
arr=[10, 3, 45, 90, 9] 
n=len(arr) 
Ans=smallest(arr,n) 
print ("smallest in given array is",Ans)
