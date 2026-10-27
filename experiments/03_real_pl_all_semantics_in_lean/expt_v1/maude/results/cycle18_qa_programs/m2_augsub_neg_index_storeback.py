a = [[1]]
def f():
    a.append(0)
    return [2]
a[-1] += f()
print(a[1])
