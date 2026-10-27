# lambdas closing over lists / dicts, called in the defining and other activations
def mk():
    xs = []
    f = lambda v: len(xs) + v
    return f
f = mk()
print(f(0))
def mk2():
    xs = []
    def push(v):
        xs.append(v)
        return len(xs)
    f = lambda v: push(v) + push(v)
    return f
g = mk2()
print(g(1))
print(g(1))
def mk3():
    d = {}
    def set(k):
        d[k] = 1
        return len(d)
    get = lambda: len(d)
    set("a")
    set("b")
    return get
h = mk3()
print(h())
adders = []
for k in range(3):
    adders.append(lambda v: v + k)
print(adders[0](10))
