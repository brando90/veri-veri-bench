def fill(acc, n):
    if n == 0:
        return acc
    acc += [n]
    return fill(acc, n - 1)
mine = []
out = fill(mine, 5)
print(len(mine))
print(out == mine)
print(mine[0] * 10 + mine[4])
def rep(acc, n):
    if n == 0:
        return 0
    acc *= 2
    return 1 + rep(acc, n - 1)
z = [1]
print(rep(z, 4))
print(len(z))
