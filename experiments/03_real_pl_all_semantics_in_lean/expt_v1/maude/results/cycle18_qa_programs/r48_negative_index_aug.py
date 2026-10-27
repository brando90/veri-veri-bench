xs = [1, [2], "s", (3,)]
xs[-4] += 1
xs[-3] += [5]
xs[-2] *= 3
xs[-1] += (4,)
print(xs)
inner = xs[-3]
xs[-3] *= 2
print(inner)
d = {-1: 5}
d[-1] += 1
print(d)
