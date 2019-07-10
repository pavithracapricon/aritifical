t1=int(input())
s1=input().split()
for i in range(len(s1)):
    for j in range(i+1,len(s1)):
        for k in range(j+1,len(s1)):
            if(int(s1[i])+int(s1[j])==int(s1[k])):
                print(s1[i],s1[j],s1[k])
