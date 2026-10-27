def f():
    n = 0
    log = []
    while n < 3:
        try:
            log.append(w)
        except Exception as e:
            log.append(-1)
        w = n
        n += 1
    return log
r = f()
for v in r:
    print(v)
