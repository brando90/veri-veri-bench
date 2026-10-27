x = 1
def f():
    try:
        r = x
    except Exception as e:
        r = "ULE"
    x = 2
    return r
print(f())
def g():
    try:
        x += 1
    except Exception as e:
        return "ULE2"
    return x
print(g())
def h():
    try:
        x[0] += 1
    except Exception as e:
        return "never"
    return "ok"
x = [5]
print(h())
print(x)
