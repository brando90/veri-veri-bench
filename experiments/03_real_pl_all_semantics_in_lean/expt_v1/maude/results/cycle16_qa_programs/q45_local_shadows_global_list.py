xs = [1, 2, 3]
def f():
    xs = []
    xs.append(9)
    return len(xs)
print(f())
print(len(xs))
def g():
    xs.append(4)
print(len(xs))
g()
print(len(xs))
