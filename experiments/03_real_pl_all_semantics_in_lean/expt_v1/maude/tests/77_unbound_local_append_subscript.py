# xs.append(..) and xs[i] = .. on a name that is local to the function but not yet assigned raise UnboundLocalError
xs = [1]
def f():
    xs.append(2)
    xs = []
try:
    f()
except Exception as e:
    print(91)
print(len(xs))
d = {"a": 1}
def g():
    d["a"] = 2
    d = {}
try:
    g()
except Exception as e2:
    print(92)
print(d["a"])
ys = [5, 6]
def h():
    ys[0] = 7
    return ys[0]
print(h())
print(ys[0])
def k():
    zs = [1]
    zs.append(3)
    zs[0] = 4
    return zs[0] + zs[1]
print(k())
