x = 1
y = 2
def f(x):
    y = x + 100
    return y
def g():
    return x + y
print(f(5))
print(g())
print(x)
print(y)
def h(a):
    x = a
    return f(x) + g()
print(h(3))
print(x)
