a = [1, 2]
b = a
a *= 0
print(len(b))
a += [3]
print(len(b))
c = [1]
c *= 1
print(len(c))
s = "ab"
s *= 0
print(len(s))
