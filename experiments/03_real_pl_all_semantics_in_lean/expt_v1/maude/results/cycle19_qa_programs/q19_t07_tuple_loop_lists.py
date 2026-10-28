t = ([], [], [])
n = 0
for i in range(3):
    try:
        t[i] += [i]
    except Exception as e:
        n += 1
print(n)
print(t)
