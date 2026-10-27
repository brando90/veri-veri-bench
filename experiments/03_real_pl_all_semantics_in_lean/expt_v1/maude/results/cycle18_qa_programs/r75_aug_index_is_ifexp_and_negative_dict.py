d = {"pos": 0, "neg": 0}
for v in [3, -1, 4, -1, -5, 9]:
    d["pos" if v > 0 else "neg"] += v
print(d)
xs = [0] * 4
for v in [1, 2, 3, 4, 5, 6, 7]:
    xs[-(v % 4) - 1] += v
print(xs)
