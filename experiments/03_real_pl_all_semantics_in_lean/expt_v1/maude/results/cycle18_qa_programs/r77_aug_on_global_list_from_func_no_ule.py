xs = [[1]]
def f():
    xs[0] += [2]
    xs[-1] *= 2
    return len(xs[0])
print(f())
print(xs)
counts = {"n": 0}
def g():
    counts["n"] += 1
g()
g()
print(counts)
