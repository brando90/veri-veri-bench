fs = []
def f(n):
    def g():
        return n * 2
    fs.append(g)
    raise Exception(n)
for i in range(3):
    try:
        f(i)
    except Exception as e:
        pass
s = 0
for h in fs:
    s += h()
print(s)
