def build(n, fs):
    if n == 0:
        return fs
    fs.append(lambda: n)
    return build(n - 1, fs)
fs = build(4, [])
print(fs[0]() * 1000 + fs[1]() * 100 + fs[2]() * 10 + fs[3]())
