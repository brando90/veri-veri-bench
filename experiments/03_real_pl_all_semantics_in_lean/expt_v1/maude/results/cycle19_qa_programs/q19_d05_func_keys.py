def f():
    return 1
def g():
    return 2
a = {f: 1, g: 2}
b = {g: 2, f: 1}
print(a == b)
print(a[f] + b[g])
