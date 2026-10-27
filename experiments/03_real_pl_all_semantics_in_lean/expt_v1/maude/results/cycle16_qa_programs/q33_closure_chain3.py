def a(x):
    def b(y):
        def c(z):
            return x * 100 + y * 10 + z
        return c
    return b
print(a(1)(2)(3))
f = a(4)
g1 = f(5)
g2 = f(6)
print(g1(7) + g2(8))
