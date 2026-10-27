a = [[1]]
def f():
    a[0] = [100]
    return [5]
a[0] += f()
print(a[0][0])
