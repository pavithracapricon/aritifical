s1  =input()
t1 = list(map(int,input().split()))
for i in range(len(t1)):
    if (i%2 == 0 and t1[i]%2 !=0) or (i%2!= 0 and t1[i]%2 == 0):
        print(t1[i],end = " ")
