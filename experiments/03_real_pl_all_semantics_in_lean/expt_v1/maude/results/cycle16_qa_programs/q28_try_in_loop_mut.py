xs = []
for i in range(6):
    try:
        xs.append(i)
        if i % 2 == 0:
            raise Exception(i)
        xs.append(100)
    except Exception as e:
        xs.append(1000)
print(len(xs))
s = 0
for v in xs:
    s += v
print(s)
