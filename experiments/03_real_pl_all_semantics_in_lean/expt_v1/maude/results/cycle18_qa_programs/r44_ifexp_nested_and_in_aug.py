xs = [0, 0, 0]
for i in range(6):
    xs[0 if i % 3 == 0 else (1 if i % 3 == 1 else -1)] += i
print(xs)
ys = [[], []]
for i in range(4):
    ys[i % 2] += [i] if i > 1 else (i,)
print(ys)
n = 5
n += 10 if n > 3 else -10
print(n)
