def f():
    total = 0
    for i in range(4):
        try:
            if i % 2 == 0:
                raise Exception(i)
            total += i
        except Exception:
            total += 100
    return total
print(f())
