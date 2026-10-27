a = [1]
a += [a]
print(len(a))
b = a[1]
print(len(b))
print(b == a)
