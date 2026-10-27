fs = []
def mk(i):
    return lambda: i
for i in range(100):
    fs.append(mk(i))
s = 0
for f in fs:
    s += f()
print(s)
