
t= float(input("Input time in seconds: "))
d = t // (24 * 3600)
t = t % (24 * 3600)
h = t // 3600
t%= 3600
m = t// 60
t %= 60
s = t
print("d:h:m:s-> %d:%d:%d:%d" % (d, h, m, s))
