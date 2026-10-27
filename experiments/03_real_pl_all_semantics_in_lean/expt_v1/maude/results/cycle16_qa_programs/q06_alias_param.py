def f(a, b):
    a.append(1)
    b.append(2)
    return len(a)
x = []
print(f(x, x))
print(len(x))
