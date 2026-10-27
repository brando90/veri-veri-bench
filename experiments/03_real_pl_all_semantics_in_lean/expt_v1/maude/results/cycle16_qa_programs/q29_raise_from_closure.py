def mk():
    log = []
    def f(v):
        log.append(v)
        if v > 2:
            raise Exception(v)
        return len(log)
    def n():
        return len(log)
    return f, n
f, n = mk()
try:
    f(1)
    f(2)
    f(3)
    f(4)
except Exception as e:
    print(e)
print(n())
