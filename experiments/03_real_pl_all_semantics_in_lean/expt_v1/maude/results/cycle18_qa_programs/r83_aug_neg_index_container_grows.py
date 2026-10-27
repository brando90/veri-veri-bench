a = [[1]]
def f():
    a.append(0)
    return [2]
a[-1] += f()
print(a)
b = [1]
def g():
    b.append(0)
    return 5
b[-1] += g()
print(b)
