def mk(i):
    return [i, i + 1]
total = 0
for i in range(200):
    l = mk(i)
    total += l[1]
print(total)
