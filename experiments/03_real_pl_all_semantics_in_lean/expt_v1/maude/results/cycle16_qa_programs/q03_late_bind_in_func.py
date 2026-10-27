def mk():
    fs = []
    for i in range(3):
        fs.append(lambda: i * 10)
    return fs
fs = mk()
print(fs[0]() + fs[1]())
