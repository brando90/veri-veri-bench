def mk(l):
    def f(v):
        l.append(v)
    return f
x = []
f = mk(x)
f(1)
f(2)
print(len(x))
g = lambda v: len(x) + v
x.append(3)
print(g(10))
