def outer():
    cnt = [0]
    def mid(k):
        cnt[0] += 1
        return inner(k)
    def inner(k):
        return k % (k - 2)
    res = []
    for k in range(5):
        try:
            res.append(mid(k))
        except Exception as e:
            res.append("Z")
    return res, cnt
r, c = outer()
print(r)
print(c)
