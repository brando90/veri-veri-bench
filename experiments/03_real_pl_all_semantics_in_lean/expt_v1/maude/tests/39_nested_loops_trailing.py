n = 0
i0 = 0
while i0 < 3:
    i0 = i0 + 1
    i1 = 0
    while i1 < 3:
        i1 = i1 + 1
        i2 = 0
        while i2 < 3:
            i2 = i2 + 1
            n = n + 1
            if i2 == 2:
                continue
            n = n + 1
        n = n + 1
        if i1 == 2:
            continue
        n = n + 1
    n = n + 1
    if i0 == 2:
        continue
    n = n + 1
print(n)
