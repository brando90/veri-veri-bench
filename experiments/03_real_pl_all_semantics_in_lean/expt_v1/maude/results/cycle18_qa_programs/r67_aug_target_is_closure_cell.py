def outer():
    acc = [[]]
    def add(v):
        acc[0] += [v]
        acc[-1] += (v * 10,)
    add(1)
    add(2)
    return acc
print(outer())
