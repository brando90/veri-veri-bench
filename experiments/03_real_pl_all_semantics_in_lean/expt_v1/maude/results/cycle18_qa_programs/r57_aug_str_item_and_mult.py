xs = ["ab", "c"]
s = xs[0]
xs[0] += "!"
xs[1] *= 3
print(xs)
print(s)
xs[0] *= 0
print(xs)
print(len(xs[0]))
