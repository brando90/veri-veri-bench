log = []
def t(v):
    log.append(v)
    return v
x = t(1) + t(2) * t(3)
print(x)
print(log[0] * 100 + log[1] * 10 + log[2])
