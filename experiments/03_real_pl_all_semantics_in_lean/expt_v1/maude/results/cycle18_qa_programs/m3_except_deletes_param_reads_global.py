e = "global"
def f(e):
    try:
        raise Exception(1)
    except Exception as e:
        pass
    return e
try:
    print(f("param"))
except Exception as z:
    print("UnboundLocalError")
