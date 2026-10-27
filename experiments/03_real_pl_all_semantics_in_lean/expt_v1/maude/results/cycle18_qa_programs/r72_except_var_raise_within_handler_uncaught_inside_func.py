def f():
    try:
        raise Exception("a")
    except Exception as e:
        raise Exception("az")
def g():
    try:
        f()
    except Exception as e:
        return e
print(g())
def h():
    e = 1
    try:
        f()
    except Exception as q:
        pass
    return e
print(h())
