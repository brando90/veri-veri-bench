def f(l):
    def add(v):
        l.append(v)
    add(1)
    add(2)
    return add
x = []
a = f(x)
a(3)
print(len(x))
