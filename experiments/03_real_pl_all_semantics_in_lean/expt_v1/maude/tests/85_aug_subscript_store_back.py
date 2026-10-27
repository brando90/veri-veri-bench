# x[i] op= e stores the result back even when the item was changed in place (CPython: x[i] = x[i].__iadd__(e))
a = [[1]]
def f():
    a[0] = [100]
    return [5]
a[0] += f()
print(a[0][0])
print(len(a[0]))

b = [[1]]
def g():
    b.append(0)
    return [2]
b[-1] += g()
print(len(b))
print(b[1][1])
print(len(b[0]))
