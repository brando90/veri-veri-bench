def outer(n):
    acc = []
    def rec(k):
        if k == 0:
            return 0
        acc.append(k)
        return k + rec(k - 1)
    s = rec(n)
    return s * 100 + len(acc)
print(outer(5))
