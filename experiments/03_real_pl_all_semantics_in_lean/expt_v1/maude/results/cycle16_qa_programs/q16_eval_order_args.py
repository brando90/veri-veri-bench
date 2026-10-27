log = []
def t(v):
    log.append(v)
    return v
def f(a, b, c):
    return a * 100 + b * 10 + c
print(f(t(1), t(2), t(3)))
print(log[0] * 100 + log[1] * 10 + log[2])
