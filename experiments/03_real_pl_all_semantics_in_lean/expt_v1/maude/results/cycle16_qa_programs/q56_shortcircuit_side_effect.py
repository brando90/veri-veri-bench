log = []
def t(v):
    log.append(v)
    return v
r = t(0) and t(1)
r2 = t(2) or t(3)
print(len(log))
print(r2)
