x = 100
def f(x):
    def g():
        return x
    return g
def h():
    return x
print(f(1)())
print(h())
