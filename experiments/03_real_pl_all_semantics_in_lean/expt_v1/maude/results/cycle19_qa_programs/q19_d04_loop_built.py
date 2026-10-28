a = {}
for k in [5, 1, 4, 2, 3]:
    a[k] = k * k
b = {}
for k in [1, 2, 3, 4, 5]:
    b[k] = k * k
print(a == b)
print(a)
b[3] = 0
print(a == b)
