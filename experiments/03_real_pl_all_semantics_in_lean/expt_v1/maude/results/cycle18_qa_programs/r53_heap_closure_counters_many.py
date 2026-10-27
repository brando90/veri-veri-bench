def make():
    box = [0]
    def inc():
        box[0] += 1
        return box[0]
    return inc
cs = []
for i in range(50):
    cs.append(make())
for i in range(50):
    for j in range(i % 4):
        cs[i]()
s = 0
for c in cs:
    s += c()
print(s)
