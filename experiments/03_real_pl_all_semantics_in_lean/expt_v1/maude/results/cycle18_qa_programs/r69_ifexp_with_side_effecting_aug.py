st = [0]
def inc():
    st[0] += 1
    return st[0]
vals = []
for i in range(5):
    vals.append(inc() if i % 2 == 0 else -inc())
print(vals)
print(st)
