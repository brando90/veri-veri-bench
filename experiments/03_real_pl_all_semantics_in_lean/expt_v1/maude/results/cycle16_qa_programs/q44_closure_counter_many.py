def mk():
    c = [0]
    def inc():
        c[0] = c[0] + 1
        return c[0]
    return inc
f = mk()
for i in range(150):
    f()
print(f())
