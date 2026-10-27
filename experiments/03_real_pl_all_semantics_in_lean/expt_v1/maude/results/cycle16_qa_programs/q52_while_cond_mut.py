xs = [3]
def step(l):
    l.append(len(l))
    return len(l) < 6
while step(xs):
    pass
print(len(xs))
