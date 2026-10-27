def f():
    try:
        raise Exception("x")
    except Exception as e:
        e = [1]
        e += [2]
        keep = e
    try:
        return e
    except Exception as z:
        return keep
print(f())
