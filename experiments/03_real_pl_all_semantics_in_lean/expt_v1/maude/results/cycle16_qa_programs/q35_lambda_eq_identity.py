fs = []
for i in range(2):
    fs.append(lambda: 0)
if fs[0] == fs[1]:
    print(1)
else:
    print(0)
