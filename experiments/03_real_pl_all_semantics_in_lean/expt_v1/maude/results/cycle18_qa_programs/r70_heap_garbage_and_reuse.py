def build(n):
    out = []
    for i in range(n):
        tmp = [i, [i]]
        tmp[1] += [i]
        out.append(tmp[1])
    return out
r = build(40)
print(r[39])
total = 0
for k in range(20):
    r2 = build(5)
    total += len(r2[4])
print(total)
