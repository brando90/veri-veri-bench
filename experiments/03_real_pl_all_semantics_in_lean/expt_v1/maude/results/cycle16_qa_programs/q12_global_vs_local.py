x = 1
def f():
    x = 2
    def g():
        return x
    return g()
def h():
    return x
print(f())
print(h())
print(x)
