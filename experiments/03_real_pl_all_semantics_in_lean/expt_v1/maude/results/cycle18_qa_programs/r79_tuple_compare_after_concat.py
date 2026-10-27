a = (1, 2) + (3,)
b = (1,) + (2, 3)
print(a == b)
print(a != (1, 2))
c = ([1],) * 2
c0 = c[0]
c0.append(2)
print(c)
print(c[0] == c[1])
