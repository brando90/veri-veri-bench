def outer():
    fs = []
    for i in range(3):
        def g():
            return k
        fs.append(g)
    k = 42
    return fs
s = 0
for f in outer():
    s += f()
print(s)
