a = [[1]]
b = a[0]
a[0] += [2]
t = (b,)
try:
    t[0] += [3]
except Exception as e:
    print("TE")
print(a)
print(b)
print(t)
print(a[0] == t[0])
