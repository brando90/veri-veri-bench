out = []
for i in range(4):
    row = []
    for j in range(i):
        row.append(j)
    out.append(row)
print(len(out[3]))
print(len(row))
row.append(9)
print(len(out[3]))
