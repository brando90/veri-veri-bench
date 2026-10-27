a = [1]
b = [2]
c = a if len(a) > 0 else b
c.append(3)
print(a)
d = (a if False else b)
d += [4]
print(b)
e = [a, b][0 if a[0] == 1 else 1]
e[0] = 99
print(a)
