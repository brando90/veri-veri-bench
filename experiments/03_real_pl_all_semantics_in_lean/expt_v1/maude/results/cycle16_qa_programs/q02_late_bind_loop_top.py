fs = []
i = 0
while i < 3:
    fs.append(lambda: i)
    i += 1
print(fs[0]())
print(fs[2]())
