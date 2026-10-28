def f():
    return 1
g = lambda: 2
a = {1: f, 2: g}
b = {2: g, 1: f}
print(a == b)
c = {1: g, 2: f}
print(a == c)
