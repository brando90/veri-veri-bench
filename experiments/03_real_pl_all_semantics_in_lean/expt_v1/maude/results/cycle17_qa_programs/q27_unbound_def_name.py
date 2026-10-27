def helper():
    return 1
def f():
    r = helper()
    def helper():
        return 2
    return r
try:
    print(f())
except Exception as e:
    print("ule")
def g():
    def helper():
        return 3
    return helper()
print(g())
print(helper())
