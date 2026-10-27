def down(n, acc):
    if n == 0:
        return acc
    acc.append(n)
    return down(n - 1, acc)
r = down(150, [])
print(len(r))
print(r[0] + r[149])
