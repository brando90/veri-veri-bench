def rec(n):
    try:
        if n == 0:
            raise Exception("base")
        return rec(n - 1) + 1
    except Exception as e:
        if n < 2:
            raise Exception(n)
        r = n
    try:
        return e
    except Exception as z:
        return r * 100
print(rec(4))
