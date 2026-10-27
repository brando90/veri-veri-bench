a = [1]
a.append(a)
print(len(a))
t = (a, 2)
if t == t:
    print(1)
else:
    print(0)
