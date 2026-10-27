# a list is one heap object: names alias it; slices, concatenations and repeats are fresh copies
xs = [1, 2, 3]
ys = xs
ys.append(4)
print(len(xs))
xs[0] = 10
print(ys[0])
zs = xs[:]
zs.append(5)
print(len(xs))
print(len(zs))
ws = xs + []
ws[1] = 99
print(xs[1])
print(ws[1])
rs = [0] * 3
rs[0] = 7
print(rs[0])
print(rs[1])
print(xs == ys)
print(xs == zs)
print(xs != zs)
print([[1], [2]] == [[1], [2]])
print([[1], [2]] == [[1], [3]])
t = (xs, 5)
xs.append(6)
print(len(t[0]))
print(t[1])
