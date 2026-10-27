inner = [1]
t = (inner, 2)
xs = []
xs += t
x0 = xs[0]
x0.append(9)
print(inner)
print(xs)
d = {"k": []}
d["k"] += (inner,)
dk = d["k"]
dk0 = dk[0]
dk0.append(3)
print(inner)
