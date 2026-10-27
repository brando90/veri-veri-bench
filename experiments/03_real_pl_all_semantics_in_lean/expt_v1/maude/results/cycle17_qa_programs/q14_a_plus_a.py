a = [1, 2]
b = a
a += a
print(len(b))
print(b[3])
a += a
print(len(b))
c = [5]
c *= 2
c += c
print(len(c))
