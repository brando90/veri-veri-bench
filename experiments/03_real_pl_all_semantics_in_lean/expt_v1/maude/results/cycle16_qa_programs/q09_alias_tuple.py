x = [1]
t = (x, x)
a = t[0]
a.append(2)
print(len(t[1]))
a, b = t
b.append(9)
print(len(x))
