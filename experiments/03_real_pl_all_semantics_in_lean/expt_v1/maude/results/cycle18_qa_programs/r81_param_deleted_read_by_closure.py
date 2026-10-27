e = "global"
def f(e):
    def g():
        return e
    try:
        raise Exception("x")
    except Exception as e:
        pass
    try:
        return g()
    except Exception as z:
        return "NameError"
print(f("param"))
