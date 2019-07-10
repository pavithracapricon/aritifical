n1 = int(input())
s1 = [x for x in input().split()]
t1 = []
for i in range(len(s1)):
    if s1[i] == str(i):
        t1.append(s1[i])

if len(t1) == 0:
    print('-1')
else:
    print(' '.join(sorted(t1)))
