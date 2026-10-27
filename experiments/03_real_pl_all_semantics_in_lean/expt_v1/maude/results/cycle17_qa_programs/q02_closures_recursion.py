def build(n):
    if n == 0:
        return []
    fs = build(n - 1)
    m = n * n
    fs.append(lambda: m + n)
    return fs
fs = build(5)
for f in fs:
    print(f())
