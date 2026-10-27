a = [1]
a.append(a)
b = [a]
b[0] += [3]
print(len(a))
print(a[2])
print(len(a[1]))
c = [0]
c[0] = c
c[0] += [4]
print(len(c))
print(c[1])
