def scan(xs):
    found = -1
    for i in range(len(xs)):
        v = xs[i]
        if v < 0:
            continue
        if v > 5:
            found = i
            break
    return found
print(scan([1, -2, 7, 9]))
print(scan([1, 2]))
def outer(n):
    res = 0
    i = 0
    while True:
        i += 1
        if i > n:
            break
        res += scan([i, 6])
    return res
print(outer(4))
