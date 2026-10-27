def mk():
    try:
        raise Exception(5)
    except Exception as e:
        print(e)
        v = 5
        return lambda: v * 2
f = mk()
print(f())
def mk2():
    try:
        raise Exception(6)
    except Exception as e:
        return lambda: e
g = mk2()
try:
    print(g())
except Exception as z:
    print("free e deleted")
