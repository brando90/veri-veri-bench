def outer():
    xs = [1]
    def add():
        ys = xs
        ys += [2]
        return len(xs)
    r = add()
    return r * 10 + len(xs)
print(outer())
def outer2():
    n = 5
    def bump():
        n += 1
        return n
    try:
        return bump()
    except Exception as e:
        return n * 100
print(outer2())
