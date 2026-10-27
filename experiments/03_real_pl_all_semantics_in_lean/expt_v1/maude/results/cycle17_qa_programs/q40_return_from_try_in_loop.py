def f(n):
    i = 0
    while i < n:
        try:
            if i == 2:
                return i * 100
            if i == 1:
                raise Exception("e")
        except Exception as e:
            i += 10
            i -= 9
            continue
        i += 1
    return -1
print(f(5))
print(f(1))
