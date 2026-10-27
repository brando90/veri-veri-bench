def a(x):
    y = x + 1
    def b(z):
        w = z * 2
        def c(q):
            return x + y + w + q
        return c
    return b
cs = []
for i in range(3):
    cs.append(a(i)(i + 10))
for c in cs:
    print(c(100))
