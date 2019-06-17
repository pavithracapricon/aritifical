def multiple(m, n):   
    a = range(n, (m * n)+1, n) 
    print(*a)  
m = int(input("number is"))
n = int(input("number is"))
multiple(m, n)
