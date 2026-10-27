def walk(n, acc):
    if n == 0:
        return acc
    acc += [n]
    acc *= 1
    return walk(n - 1, acc)
base = []
r = walk(5, base)
print(base)
def walk_t(n, acc):
    if n == 0:
        return acc
    acc += (n,)
    return walk_t(n - 1, acc)
bt = ()
print(walk_t(4, bt))
print(bt)
