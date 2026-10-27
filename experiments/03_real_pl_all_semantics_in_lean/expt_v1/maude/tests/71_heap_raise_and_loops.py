# mutations made before a raise survive it; closures made in loops share the loop variable
def risky(xs):
    xs.append(1)
    if len(xs) > 2:
        raise Exception(7)
    xs.append(2)
    return len(xs)
acc = []
try:
    risky(acc)
    risky(acc)
except Exception as e:
    print(e)
print(len(acc))
fs = []
for i in range(3):
    fs.append(lambda: i)
print(fs[0]() + fs[1]() + fs[2]())
def build():
    out = []
    for j in range(3):
        def g():
            return j
        out.append(g)
    j = 10
    return out
bs = build()
print(bs[0]() + bs[2]())
total = []
def collect(n):
    k = 0
    while k < n:
        total.append(k)
        k = k + 1
        if k == 3:
            break
    return len(total)
print(collect(5))
print(collect(2))
print(len(total))
def f(xs):
    xs.append(0)
    return xs
ys = f(f([]))
print(len(ys))
