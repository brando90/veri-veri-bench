def outer():
    x = 1
    def inner():
        x = 2
        return x
    r = inner()
    return r * 10 + x
print(outer())
