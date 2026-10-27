def f():
    n = 0
    while n < 3:
        try:
            raise Exception(n)
        except Exception as e:
            n = n + 1
    try:
        return e
    except Exception as z:
        return n * 100
print(f())
