a,b=map(int,input().split())
for w in range(a+1,b):
	s=0
	i=w
	while(i>0):
		c=i%10
		s+=c**3
		i//=10
	if(w==i):
		print(w,end=" ")
