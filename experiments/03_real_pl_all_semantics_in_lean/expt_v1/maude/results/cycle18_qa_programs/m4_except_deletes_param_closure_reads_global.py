e = "global"
def f(e):
    def g():
        return e
    try:
        raise Exception(1)
    except Exception as e:
        pass
    return g()
try:
    print(f("param"))
except Exception as z:
    print("NameError")
