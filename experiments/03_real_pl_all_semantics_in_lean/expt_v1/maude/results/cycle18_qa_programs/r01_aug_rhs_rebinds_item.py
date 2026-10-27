a = [[1], [2]]
orig = a[0]
def f():
    a[0] = [100]
    return [5]
a[0] += f()
print(a)
print(orig)
