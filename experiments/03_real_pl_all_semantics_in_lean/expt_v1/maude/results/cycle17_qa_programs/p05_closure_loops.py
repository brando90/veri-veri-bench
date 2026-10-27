def adder(k):
    return lambda v: v + k
fs = []
for i in range(30):
    fs.append(adder(i))
acc = 0
for r in range(5):
    for f in fs:
        acc = f(acc) % 1000
print(acc)
