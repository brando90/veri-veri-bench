def outer():
    x = 1
    f = lambda: x
    x = 2
    r1 = f()
    x += 5
    return r1 * 10 + f()
print(outer())
def outer2():
    xs = [1]
    f = lambda: len(xs)
    xs += [2, 3]
    return f()
print(outer2())
