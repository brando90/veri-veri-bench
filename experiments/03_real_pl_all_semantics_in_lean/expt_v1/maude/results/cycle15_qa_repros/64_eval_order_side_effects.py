# left-to-right evaluation with side effects visible to later operands
log = []
def rec(v):
    log.append(v)
    return len(log)
xs = [rec(1), len(log), rec(2), len(log)]
print(xs[1])
print(xs[3])
print(len(log) + rec(3))
print(rec(4) + len(log))
d = {rec(5): len(log), len(log): rec(6)}
print(d[5])
print(len(d))
t = (rec(7), len(log))
print(t[1])
print(log[rec(8) - 1])
ys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(ys[rec(9) - 9:rec(10)]))
print(len(log))
