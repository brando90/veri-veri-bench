def f():
    try:
        raise Exception("x")
    except Exception as e:
        pass
    try:
        return e
    except Exception as e2:
        return "ule"
print(f())
