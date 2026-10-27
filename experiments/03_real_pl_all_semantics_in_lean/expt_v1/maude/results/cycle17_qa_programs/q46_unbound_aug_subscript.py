xs = [5]
def f():
    xs[0] += 1
    xs = [1]
    return xs[0]
try:
    print(f())
except Exception as e:
    print("ule")
print(xs[0])
def g():
    xs[0] += 1
    return xs[0]
print(g())
print(xs[0])
