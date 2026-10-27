# f(g(xs)) where g mutates xs and returns it, f mutates the same list again
def g(xs):
    xs.append(1)
    return xs
def f(ys):
    ys.append(2)
    return len(ys)
a = []
print(f(g(a)))
print(len(a))
def h(ys):
    ys.append(2)
    return len(ys)
store = []
def push(v):
    store.append(v)
    return len(store)
print(h([push(1), push(2)]))
print(len(store))
print(push(len(store)) + push(0))
print(store[2])
