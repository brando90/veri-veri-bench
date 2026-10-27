log = []
def rec(v):
    log.append(v)
    return len(log)
d = {rec(5): len(log), len(log): rec(6)}
print(d[1])
print(len(d))
e = {1: 10, 1: 20, 2: 30}
print(e[1])
print(len(e))
