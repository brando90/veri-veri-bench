objs = []
i = 0
while i < 2000:
    objs.append([i % 13])
    i += 1
total = 0
for o in objs:
    total += o[0]
print(total)
pairs = []
for j in range(0, 2000, 97):
    pairs.append(objs[j])
for p in pairs:
    p += [1]
s = 0
for j in range(0, 2000, 97):
    s += len(objs[j])
print(s)
