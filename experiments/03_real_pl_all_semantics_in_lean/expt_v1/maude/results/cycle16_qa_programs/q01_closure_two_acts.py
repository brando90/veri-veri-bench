def mk(n):
    def g():
        return n
    return g
a = mk(1)
b = mk(2)
print(a() + b() * 10)
