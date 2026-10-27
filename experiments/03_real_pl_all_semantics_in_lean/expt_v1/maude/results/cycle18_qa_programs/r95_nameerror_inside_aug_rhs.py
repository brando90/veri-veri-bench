xs = [[1]]
alias = xs[0]
try:
    xs[0] += [undefined_thing]
except Exception as e:
    print("NE")
print(alias)
def f():
    try:
        xs[0] += later_global
    except Exception as e:
        return "NE2"
    return "ok"
print(f())
later_global = (7,)
print(f())
print(xs)
