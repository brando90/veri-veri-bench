xs = [1, 2]
n = 0
for v in xs:
    if v < 5:
        xs.append(v + 3)
    n += 1
print(n)
print(len(xs))
