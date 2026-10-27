a = [[1], [2]]
inner = a[0]
a[0] += [9]
print(len(inner))
print(len(a[0]))
