# one list passed to two parameters of the same call
def f(a, b):
    a.append(1)
    b.append(2)
    return len(a) + len(b)
xs = [0]
print(f(xs, xs))
print(len(xs))
print(xs[1])
print(xs[2])
