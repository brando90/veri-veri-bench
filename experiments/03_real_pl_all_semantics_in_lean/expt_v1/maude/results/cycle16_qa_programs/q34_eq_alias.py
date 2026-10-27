a = [1, [2, 3]]
b = [1, [2, 3]]
if a == b:
    print(1)
else:
    print(0)
c = a
t = c[1]
t[0] = 9
if a == b:
    print(1)
else:
    print(0)
