# `except ... as p` on a parameter p deletes it after the handler
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

def h(e):
    def g():
        return e
    try:
        raise Exception(1)
    except Exception as e:
        pass
    return g()
try:
    print(h("param"))
except Exception as z:
    print("NameError")

xs = []
def k(xs):
    try:
        raise Exception(1)
    except Exception as xs:
        pass
    xs.append(1)
try:
    k([0])
except Exception as z:
    print("UnboundLocalError")
print(len(xs))
