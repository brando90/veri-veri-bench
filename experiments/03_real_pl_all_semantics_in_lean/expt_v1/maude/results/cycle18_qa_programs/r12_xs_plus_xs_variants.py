xs = [1, 2]
ys = xs
xs += xs
print(ys)
xs += xs[1:]
print(xs)
zs = [[0]]
zs[0] += zs[0]
print(zs)
w = [1]
w *= 3
w += w
print(w)
