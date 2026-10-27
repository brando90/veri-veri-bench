def outer():
    v = 1
    def inner():
        v = 2
        return v
    r = inner()
    return v * 10 + r
print(outer())
def outer2():
    v = 5
    def inner2():
        try:
            r = v
        except Exception as e:
            r = 77
        v = 3
        return r
    return inner2() + v
print(outer2())
