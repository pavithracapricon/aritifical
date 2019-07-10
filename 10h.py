t1,s1=map(int,input().split())
x1=list(map(int,input().split()))
y1=list(map(int,input().split()))
if set(y1).issubset(set(x1)):
    print("YES")
else:
    print("NO")
