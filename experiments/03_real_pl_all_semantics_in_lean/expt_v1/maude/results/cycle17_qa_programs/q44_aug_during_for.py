xs = [1, 2]
for x in xs:
    if len(xs) < 6:
        xs += [x * 10]
print(len(xs))
for v in xs:
    print(v)
