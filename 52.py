def num999(n):
    c = n % 10 
    b = ((n % 100) - c) / 10 
    a = ((n % 1000) - (b * 10) - c) / 100 
    t = ""
    h = ""
    if a != 0 and b == 0 and c == 0:
        t = ones[a] + "hundred "
    elif a != 0:
        t = ones[a] + "hundred and "
    if b <= 1:
        h = ones[n%100]
    elif b > 1:
        h = twenties[b] + ones[c]
    st = t + h
    return st
