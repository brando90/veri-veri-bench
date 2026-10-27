def gen(n):
    return (n, n + 1) if n >= 0 else ()
xs = []
for i in range(3):
    xs += gen(i)
print(xs)
def keys(d):
    return d
xs += keys({"z": 0, "y": 1})
print(xs)
