xs = []
for i in range(5):
    ys = xs
    ys.append(i)
print(len(xs))
s = 0
for v in xs:
    s += v
print(s)
