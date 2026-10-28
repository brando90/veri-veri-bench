def f(xs):
    try:
        return xs[10]
    except Exception as e:
        return {}["missing"]
try:
    f([1])
except Exception as e:
    print("outer")
def g():
    try:
        return 1 // 0
    except Exception as e:
        raise Exception("again")
try:
    g()
except Exception as e:
    print("outer2")
