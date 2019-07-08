    
inputs=input()
z=['a','e','i','o','u']
a=any(c in inputs for c in z)
if(a==True):
  print('yes')
else:
  print('no')
