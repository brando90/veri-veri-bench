xs = [(1, 2), (3,)]
xs[0] += (9,)
xs[1] *= 2
print(xs)
d = {"t": ()}
for i in range(3):
    d["t"] += (i,)
print(d["t"])
keep = xs[0]
xs[0] += (0,)
print(keep)
print(xs[0])
