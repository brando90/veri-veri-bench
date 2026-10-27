def mk():
    fs = []
    i = 0
    while i < 3:
        fs.append(lambda: i)
        i += 1
    return fs
for f in mk():
    print(f())
def mk2():
    fs = []
    for j in range(3):
        def g(j):
            return lambda: j * 2
        fs.append(g(j))
    return fs
for f in mk2():
    print(f())
