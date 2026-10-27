e = "global"
def f(e):
    try:
        raise Exception("inner")
    except Exception as e:
        pass
    try:
        return e
    except Exception as z:
        return "unbound"
print(f("param"))
print(e)
