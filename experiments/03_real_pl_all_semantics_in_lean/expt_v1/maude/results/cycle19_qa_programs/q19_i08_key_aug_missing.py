d = {1: 10}
for k in [1, 2, 1, 3]:
    try:
        d[k] += 1
    except Exception as e:
        d[k] = 0
print(d)
