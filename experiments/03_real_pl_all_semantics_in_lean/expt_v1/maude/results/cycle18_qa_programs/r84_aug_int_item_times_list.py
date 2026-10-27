xs = [2, "ab", (1,)]
xs[0] *= [1, 2]
print(xs)
inner = xs[0]
xs[0] += [3]
print(inner)
xs[1] *= 2
xs[2] *= 3
print(xs)
