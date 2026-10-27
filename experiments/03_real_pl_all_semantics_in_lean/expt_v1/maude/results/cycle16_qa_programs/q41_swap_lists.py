a = [1]
b = [2, 2]
a, b = b, a
a.append(3)
print(len(a))
print(len(b))
